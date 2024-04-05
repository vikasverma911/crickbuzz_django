from django.urls import path
from .views import AdminLoginAPIView, AdminSignupAPIView, MatchDetailAPIView, MatchListCreateAPIView, PlayerStatisticsAPIView, SquadMemberCreateAPIView

urlpatterns = [
    path('api/admin/signup', AdminSignupAPIView.as_view(), name='admin-signup'),
    path('api/admin/login/', AdminLoginAPIView.as_view(), name='admin-login'),
    path('api/matches/', MatchListCreateAPIView.as_view(), name='match-list-create'),
    path('api/matches/<int:match_id>/', MatchDetailAPIView.as_view(), name='match-detail'),
    path('api/teams/<int:team_id>/squad/', SquadMemberCreateAPIView.as_view(), name='add-squad-member'),
    path('api/players/<int:player_id>/stats/', PlayerStatisticsAPIView.as_view(), name='player-stats'),
]