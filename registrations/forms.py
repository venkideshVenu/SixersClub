from django import forms
from .models import TournamentRegistration
from django.contrib.auth import get_user_model
from tournaments.models import Tournament
User = get_user_model()

class IndividualRegistrationForm(forms.Form):
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())
    player_id = forms.CharField(max_length=10)

    def clean_player_id(self):
        player_id = self.cleaned_data.get('player_id')
        if not User.objects.filter(player_id=player_id).exists():
            raise forms.ValidationError("Player ID does not exist.")
        return player_id


class TournamentRegistrationForm(forms.ModelForm):
    player_ids = forms.CharField(
        label='Player IDs (comma-separated)',
        help_text="Enter Player IDs to add, separated by commas."
    )

    class Meta:
        model = TournamentRegistration
        fields = ['tournament', 'team_name', 'player_ids']  # Removed players from here

    def clean_player_ids(self):
        player_ids = self.cleaned_data.get('player_ids')
        ids = [id.strip() for id in player_ids.split(',')]
        players = User.objects.filter(player_id__in=ids)

        if not players.exists():
            raise forms.ValidationError("No valid players found with the provided IDs.")

        return players

    def save(self, commit=True):
        registration = super().save(commit=False)
        registration.save()
        # Add players to the registration
        players = self.cleaned_data.get('player_ids')
        for player in players:
            registration.players.add(player)
        if commit:
            registration.save()
        return registration
