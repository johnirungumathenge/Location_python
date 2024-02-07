from django.shortcuts import render, redirect
import folium
import geocoder
from .models import Search
from .forms import SearchForn
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "POST":
        form = SearchForn(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    else:
        form = SearchForn()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    if lat == None or lng == None:
        address.delete()
        return HttpResponse('input is invalid')

    # create map object
    m = folium.Map(location=[19,-12], zoom_start=2)
    #folium.Marker([0.053543, 37.648399], tooltip='click for more', popup="Meru").add_to(m)
    # next marker
    folium.Marker([lat,lng], tooltip='click for more', popup=country).add_to(m)
    # Get Html representation
    m = m._repr_html_()
    context = {
        'm':m,
        'form':form
    }
    return render(request, 'index.html', context)
