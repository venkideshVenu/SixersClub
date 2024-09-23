from django.urls import path
from .views import team_registration_view, individual_registration_view

urlpatterns = [
    path('team_registration/', team_registration_view, name='team_registration'),
    path('individual_registration/', individual_registration_view, name='individual_registration'),
]
