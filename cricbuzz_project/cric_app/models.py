from django.contrib.auth.models import AbstractUser
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    player_id = models.CharField(max_length=20, unique=True)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    matches_played = models.PositiveIntegerField(default=0)
    runs = models.PositiveIntegerField(default=0)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    strike_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    

    def __str__(self):
        return self.name

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1_matches')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2_matches')
    date = models.DateField()
    venue = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='upcoming')
