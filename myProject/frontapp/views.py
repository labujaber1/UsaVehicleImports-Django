from django.shortcuts import get_object_or_404, render
from .models import Vehicle, Images, Post
from django.http import HttpResponse
from django.http import Http404


# Create your views here.

# test


def home(request):

    return render(request, 'Home.html')


def services(request):

    return render(request, 'Services.html')


def gallery(request):
    try:
        vehicle_images = Images.objects.all()
        vehicles = Vehicle.objects.all()
    except Images.DoesNotExist:
        raise Http404("Sorry vehicle not found")
    return render(request, 'Gallery.html', {'vehicle_images': vehicle_images, 'vehicle': vehicles})


def news(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Sorry no posts found, I know not why but only was is!")

    return render(request, 'News.html', {'posts': posts})
