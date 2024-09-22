from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/team_manager/', views.team_manager_dashboard, name='team_manager_dashboard'),
    path('dashboard/player/', views.player_dashboard, name='player_dashboard'),
    path('dashboard/fan/', views.fan_dashboard, name='fan_dashboard'),
]
