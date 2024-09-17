# tournaments/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Team, Player

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'captain', 'contact_email', 'contact_phone']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'date_of_birth', 'role']

PlayerFormSet = inlineformset_factory(Team, Player, form=PlayerForm, extra=11, max_num=15)