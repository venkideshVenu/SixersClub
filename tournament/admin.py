from django.contrib import admin
from .models import Tournament, Team, TournamentRegistration,  Player

admin.register(Tournament, Team, TournamentRegistration, Player)(admin.ModelAdmin)