from django.shortcuts import render, redirect
import datetime as dt 
from django.http import HttpResponse, Http404
from .models import Image

# Create your views here.
def pictures(request):
    image = Image.objects.all()
    return render(request, 'pictures.html', {"image":image})

def single_image(request,image_id):
    image = Image.objects.get(id = image_id) 
    return render(request, "image.html", {"image":image})        

    
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term yet"
        return render(request, 'search.html',{"message":message})

