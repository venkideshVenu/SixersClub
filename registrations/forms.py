from django import forms
from .models import TeamRegistration, PlayerRegistration
from accounts.models import CustomUser

class TeamRegistrationForm(forms.ModelForm):
    player_ids = forms.CharField(widget=forms.Textarea, help_text="Enter player IDs separated by commas")

    class Meta:
        model = TeamRegistration
        fields = ['team_name', 'team_motto', 'player_ids']

    def clean_player_ids(self):
        player_ids = self.cleaned_data.get('player_ids').split(',')
        players = []
        for player_id in player_ids:
            try:
                player = CustomUser.objects.get(player_id=player_id.strip())
                if player.user_type != 'player':
                    raise forms.ValidationError(f"{player.username} is not a valid player.")
                players.append(player)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError(f"Player ID {player_id} does not exist.")
        return players

    def save(self, commit=True):
        instance = super().save(commit=False)
        players = self.cleaned_data['player_ids']
        if commit:
            instance.save()
            instance.players.set(players)
        return instance

from django import forms
from .models import PlayerRegistration
from accounts.models import CustomUser

class PlayerRegistrationForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('batsman', 'Batsman'),
        ('bowler', 'Bowler'),
        ('allrounder', 'All-Rounder'),
        ('wicketkeeper', 'Wicket Keeper'),
    ]

    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = PlayerRegistration
        fields = ['name', 'age', 'gender', 'role']
