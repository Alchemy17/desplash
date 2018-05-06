from django.shortcuts import render, redirect
from .models import Image, Category, Location
import datetime as dt
from django.http  import HttpResponse
# Create your views here.
def welcome(request):
    title = 'Home'
    date = dt.date.today
    photos = Image.get_all()
    return render(request, 'home.html',
                  {"title": title,
                   "date": date,
                   "photos": photos})


def search_results(request):

    if 'gallery' in request.GET and request.GET["gallery"]:
        search_term = request.GET.get("gallery")
        searched_images = Category.searched(search_term)
        images= Image.get_Image_by_category(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"gallery": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def location(request, location_id):

    locations = Image.objects.filter(location__location__icontains=location_id)
    return render(request,"location.html", {"locations":locations})