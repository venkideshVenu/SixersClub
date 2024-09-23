from django.urls import path
from . import views

urlpatterns = [
    path('register_type/', views.register_type, name='register_type'),
    path('register/', views.register_view, name='register'),
    path('register/team-manager/', views.team_manager_register_view, name='register_team_manager'),
    path('register/player/', views.player_register_view, name='register_player'),
    path('register/fan/', views.fan_register_view, name='register_fan'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/team_manager/', views.team_manager_dashboard, name='team_manager_dashboard'),
    path('dashboard/player/', views.player_dashboard, name='player_dashboard'),
    path('dashboard/fan/', views.fan_dashboard, name='fan_dashboard'),
]
