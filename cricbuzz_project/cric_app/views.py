from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Match, Player, Team
from .serializers import AdminLoginSerializer, AdminSignupSerializer, MatchDetailSerializer, MatchSerializer, PlayerSerializer, PlayerStatisticsSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@permission_classes([AllowAny])
class AdminSignupAPIView(APIView):
    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"status": "Admin Account successfully created", "status_code": 200, "user_id": user.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class AdminLoginAPIView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"status": "Login successful", "status_code": 200, "user_id": user.id, "access_token": token.key})
            else:
                return Response({"status": "Incorrect username/password provided. Please retry", "status_code": 401})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchListCreateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        team_1_name = request.data.get('team_1')
        team_2_name = request.data.get('team_2')
        date = request.data.get('date')
        venue = request.data.get('venue')

        team_1, created_1 = Team.objects.get_or_create(name=team_1_name)
        team_2, created_2 = Team.objects.get_or_create(name=team_2_name)

        match = Match.objects.create(team_1=team_1, team_2=team_2, date=date, venue=venue)

        serializer = MatchSerializer(match)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response({"matches": serializer.data})
    
class MatchDetailAPIView(APIView):
    def get(self, request, match_id):
        try:
            match = Match.objects.get(match_id=match_id)
        except Match.DoesNotExist:
            return Response({"error": "Match not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MatchDetailSerializer(match)
        return Response(serializer.data)
    
class SquadMemberCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(team=team)
            return Response({"message": "Player added to squad successfully", "player_id": serializer.data['player_id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PlayerStatisticsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, player_id):
        try:
            player = Player.objects.get(player_id=player_id)
        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlayerStatisticsSerializer(player)
        return Response(serializer.data)