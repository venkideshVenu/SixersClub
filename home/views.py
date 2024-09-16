
from django.shortcuts import render
from django.http import HttpResponse

def get_home_page(request):
    return render(request, 'home/homepage.html',context={})
