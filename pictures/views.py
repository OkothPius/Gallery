from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt 

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pictures(request):
    return render(request, 'pictures.html')
    
def search_results(request):
    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Pictures.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term yet"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()    
    return render(request, "image.html", {"image":image})        
