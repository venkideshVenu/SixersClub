from django.shortcuts import render, get_object_or_404
from .models import Tournament

# List all tournaments
def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournament_list.html', {'tournaments': tournaments})

# Tournament detail view
def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'tournaments/tournament_detail.html', {'tournament': tournament})
