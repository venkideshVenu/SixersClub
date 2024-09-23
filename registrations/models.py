from django.db import models
from django.conf import settings
from tournaments.models import Tournament  # Ensure this imports the Tournament model

class TournamentRegistration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='captain_registrations')
    team_name = models.CharField(max_length=100)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='player_registrations')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_name} registered for {self.tournament.name}"

    class Meta:
        unique_together = ('tournament', 'team_name')  # Ensure a team can register only once for a tournament
