from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
from django.contrib import messages


def register_type(request):
    return render(request, 'accounts/register_types.html', context={})

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django import forms

# For Team Manager Registration
def team_manager_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'team_manager'
            user.save()
            return redirect('team_manager_dashboard')
    else:
        # Exclude 'role' field for Team Manager
        form = CustomUserCreationForm()
        form.fields['role'].widget = forms.HiddenInput()
    
    return render(request, 'accounts/register_team_manager.html', {'form': form})

# For Player Registration
def player_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'player'
            user.save()
            return redirect('player_dashboard')
    else:
        form = CustomUserCreationForm()
        # Player needs all fields, so no fields will be hidden
    
    return render(request, 'accounts/register_player.html', {'form': form})

# For Fan Registration
def fan_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'fan'
            user.save()
            return redirect('fan_dashboard')
    else:
        # Exclude 'role' and 'experience_level' fields for Fan
        form = CustomUserCreationForm()
        form.fields['role'].widget = forms.HiddenInput()
        form.fields['experience_level'].widget = forms.HiddenInput()
    
    return render(request, 'accounts/register_fan.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_team_manager:
                return redirect('team_manager_dashboard')
            elif user.is_player:
                return redirect('player_dashboard')
            else:
                return redirect('fan_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_team_manager:
                    return redirect('team_manager_dashboard')
                elif user.is_player:
                    return redirect('player_dashboard')
                else:
                    return redirect('fan_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')


@login_required
def team_manager_dashboard(request):
    if request.user.user_type != 'team_manager':
        messages.error(request, "You can;t access this dashboard.")
        return redirect('login')  # Redirect to an login access page or home page
    return render(request, 'accounts/team_manager_dashboard.html')

@login_required
def player_dashboard(request):
    if request.user.user_type != 'player':
        messages.error(request, "You can;t access this dashboard.")
        return redirect('login')
    return render(request, 'accounts/player_dashboard.html')

@login_required
def fan_dashboard(request):
    if request.user.user_type != 'fan':
        messages.error(request, "You can;t access this dashboard.")
        return redirect('login')
    return render(request, 'accounts/fan_dashboard.html')
