from django.shortcuts import render, redirect
import datetime as dt 
from django.http import HttpResponse, Http404
from .models import Image

# Create your views here.
def welcome(request):
    welcome = Welcome.objects.all()
    return render(request, 'welcome.html', {"welcome":welcome})

def pictures(request):
    image = Image.objects.all()
    return render(request, 'pictures.html', {"image":image})

def image(request,image_id):
    image = Image.objects.get(id = image_id) 
    return render(request, "image.html", {"image":image})        

    
def search_results(request):
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = images.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term yet"
        return render(request, 'search.html',{"message":message})

