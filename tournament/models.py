from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    TOURNAMENT_TYPES = (
        ('T20', 'T20'),
        ('ODI', 'One Day International'),
        ('TEST', 'Test Match'),
    )
    name = models.CharField(max_length=100)
    tournament_type = models.CharField(max_length=4, choices=TOURNAMENT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    registration_deadline = models.DateField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Player(models.Model):
    PLAYER_ROLES = (
        ('BAT', 'Batsman'),
        ('BWL', 'Bowler'),
        ('AR', 'All-Rounder'),
        ('WK', 'Wicket-Keeper'),
    )
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=3, choices=PLAYER_ROLES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name

class TournamentRegistration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='registrations')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team.name} - {self.tournament.name}"