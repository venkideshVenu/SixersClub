from django.urls import path
from . import views

urlpatterns = [
    path('team_register/<int:tournament_id>/', views.team_registration_view, name='team_register'),
    path('player_register/<int:tournament_id>/', views.player_registration_view, name='player_register'),
]
