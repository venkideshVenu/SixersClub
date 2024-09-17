from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('types', views.tournament_typoe, name="tournamentTypes"),
    path('list', views.tournament_list, name="tournamentList"),
    path('details', views.tournament_detail, name="tournamentDetail"),
    path('register', views.tournament_registration, name="tournamentRegister"),
]
