from rest_framework import serializers
from .models import Team, Player, Match
from django.contrib.auth.models import User

class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        return data

class MatchSerializer(serializers.ModelSerializer):
    team_1 = serializers.CharField(source='team_1.name')
    team_2 = serializers.CharField(source='team_2.name')

    class Meta:
        model = Match
        fields = ['match_id', 'team_1', 'team_2', 'date', 'venue']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'name']
    
    def create(self, validated_data):
        return Player.objects.create(**validated_data)

class MatchDetailSerializer(serializers.ModelSerializer):
    team_1_squad = PlayerSerializer(many=True, source='team_1.players')
    team_2_squad = PlayerSerializer(many=True, source='team_2.players')
    team_1 = serializers.CharField(source='team_1.name')
    team_2 = serializers.CharField(source='team_2.name')

    class Meta:
        model = Match
        fields = ['match_id', 'team_1', 'team_2', 'date', 'venue', 'status', 'team_1_squad', 'team_2_squad']


class PlayerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'name', 'matches_played', 'runs', 'average', 'strike_rate']