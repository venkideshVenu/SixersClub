from django.shortcuts import render, redirect
from .models import TournamentRegistration
from .forms import TournamentRegistrationForm, IndividualRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model

@login_required
def individual_registration_view(request):
    if request.method == 'POST':
        form = IndividualRegistrationForm(request.POST)
        if form.is_valid():
            tournament = form.cleaned_data['tournament']
            player_id = form.cleaned_data['player_id']
            # Get the player by player_id from the custom user model
            try:
                player = User.objects.get(player_id=player_id)
                tournament_registration = TournamentRegistration.objects.get(tournament=tournament, captain=request.user)
                tournament_registration.players.add(player)  # Add player to the team
                messages.success(request, "You have registered your interest to participate!")
                return redirect('homepage')
            except User.DoesNotExist:
                messages.error(request, "Player ID does not exist.")
            except TournamentRegistration.DoesNotExist:
                messages.error(request, "You have not registered a team for this tournament.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = IndividualRegistrationForm()

    return render(request, 'registrations/individual_registration.html', {'form': form})


@login_required
def team_registration_view(request):
    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.captain = request.user
            registration.save()
            player_ids = form.cleaned_data['player_ids']
            for player in player_ids:
                user = User.objects.get(player_id=player)
                registration.players.add(user)  # Add the user to the registration
            messages.success(request, "Team registered successfully!")
            return redirect('homepage')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TournamentRegistrationForm()

    return render(request, 'registrations/team_registration.html', {'form': form})
