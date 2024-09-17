# tournaments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tournament, Team, Player, TournamentRegistration
from .forms import TeamRegistrationForm, PlayerFormSet

def tournament_typoe(request):
    return render(request, 'tournament/tournament_types.html', context={})

def tournament_list(request):
    tournaments = Tournament.objects.all().order_by('start_date')
    return render(request, 'tournament/tournament_list.html', {'tournaments': tournaments})

def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    return render(request, 'tournament/tournament_detail.html', {'tournament': tournament})

def tournament_registration(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    
    if request.method == 'POST':
        team_form = TeamRegistrationForm(request.POST)
        player_formset = PlayerFormSet(request.POST)
        
        if team_form.is_valid() and player_formset.is_valid():
            team = team_form.save()
            players = player_formset.save(commit=False)
            for player in players:
                player.team = team
                player.save()
            
            TournamentRegistration.objects.create(tournament=tournament, team=team)
            
            messages.success(request, 'Successfully registered for the tournament!')
            return redirect('tournament_detail', tournament_id=tournament.id)
    else:
        team_form = TeamRegistrationForm()
        player_formset = PlayerFormSet()
    
    context = {
        'tournament': tournament,
        'team_form': team_form,
        'player_formset': player_formset,
    }
    return render(request, 'tournament/tournament_registration.html', context)