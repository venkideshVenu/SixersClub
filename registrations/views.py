from django.shortcuts import render, redirect
from .forms import TeamRegistrationForm, PlayerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TeamRegistration, PlayerRegistration

@login_required
def team_registration_view(request, tournament_id):
    if not request.user.is_team_manager:
        return redirect('home')  # Redirect if the user is not a team manager
    
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            team_registration = form.save(commit=False)
            team_registration.captain = request.user
            team_registration.tournament_id = tournament_id
            team_registration.save()
            form.save_m2m()  # Save the players for the ManyToMany field
            messages.success(request, 'Team registered successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Failed to register the team. Please fix the errors below.')
    else:
        form = TeamRegistrationForm()

    return render(request, 'registrations/team_register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PlayerRegistrationForm
from .models import PlayerRegistration
from tournaments.models import Tournament

@login_required
def player_registration_view(request, tournament_id):
    if not request.user.is_player:
        return redirect('home')  # Only players can access this form

    tournament = Tournament.objects.get(id=tournament_id)  # Get the tournament from the ID

    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            player_registration = form.save(commit=False)
            player_registration.player = request.user
            player_registration.tournament = tournament  # Assign the tournament passed via URL
            player_registration.save()
            messages.success(request, 'You have registered successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Failed to register. Please fix the errors below.')
    else:
        form = PlayerRegistrationForm()
    return render(request, 'registrations/player_register.html', {'form': form, 'tournament': tournament})