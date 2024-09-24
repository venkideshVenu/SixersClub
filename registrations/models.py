from django.db import models
from tournaments.models import Tournament
from accounts.models import CustomUser

class TeamRegistration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='team_registrations')
    team_name = models.CharField(max_length=100)
    team_motto = models.CharField(max_length=255, blank=True)
    captain = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managed_teams')
    players = models.ManyToManyField(CustomUser, related_name='teams', limit_choices_to={'user_type': 'player'})
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.team_name} - {self.tournament.name}"

    def validate_team(self):
        # Ensure team has the correct number of players and roles
        if self.players.count() < 11:  # Example validation, ensure at least 11 players
            raise ValueError("A team must have at least 11 players.")
        if not any(player.role == 'Batsman' for player in self.players.all()):
            raise ValueError("A team must have at least one Batsman.")
        # Add other role checks like Bowler, etc.

from django.db import models
from tournaments.models import Tournament
from accounts.models import CustomUser

class PlayerRegistration(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='registrations')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='player_registrations')
    name = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True)
    role = models.CharField(max_length=30, blank=True, null=True)  # This comes from the player role in the CustomUser table
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} - {self.tournament.name}"
