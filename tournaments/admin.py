from django.contrib import admin
from .models import Tournament

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament_type', 'start_date', 'end_date', 'registration_deadline', 'registration_fee')
    list_filter = ('tournament_type', 'start_date')
    search_fields = ('name',)
