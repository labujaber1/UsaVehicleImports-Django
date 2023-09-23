from django.shortcuts import render
from .models import Vehicle
# Create your views here.

# test


def home(request):

    return render(request, 'Home.html')


def services(request):

    return render(request, 'Services.html')


def gallery(request):

    return render(request, 'Gallery.html')
