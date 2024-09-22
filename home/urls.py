from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name="homepage"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
