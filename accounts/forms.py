from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('batsman', 'Batsman'),
        ('bowler', 'Bowler'),
        ('allrounder', 'All-Rounder'),
        ('wicketkeeper', 'Wicket Keeper'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'experience_level', 'role', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        experience_level = cleaned_data.get("experience_level")
        role = cleaned_data.get("role")

        # Ensure experience_level is required for both players and team managers
        if user_type in ['player', 'team_manager'] and not experience_level:
            self.add_error('experience_level', 'Experience level is required for players and team managers.')

        # Ensure role is required for players only
        if user_type == 'player' and not role:
            self.add_error('role', 'Role is required for players.')

        # Clear role if the user is not a player
        if user_type != 'player':
            cleaned_data['role'] = None

        return cleaned_data
    

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['user_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['experience_level'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
