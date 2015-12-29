from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from .models import Venue, CinemaLocs
from .getMap import get_place_id
from .getWeather import get_weather_data
from .getCinemaLocations import get_cinema_locations
from .getCinemas import get_cinemas
from django.utils import timezone


def index(request):
 latest_venue_list = Venue.objects.order_by('-venue_Updated')[:5]
 rated_venue_list = Venue.objects.order_by('-venue_Rating')[:5]
 random_venue_list = Venue.objects.order_by('?')[:5]
 context = {'latest_venue_list': latest_venue_list, 'rated_venue_list': rated_venue_list,
            'random_venue_list':random_venue_list}
 return render(request, 'travel/index.html', context)


def results(request):
 query = request.GET['location'].replace(',', '').split()

 location = query[0]

 weather_data = get_weather_data(location)
 place_id = get_place_id(location)

 if len(query) == 1:

    latest_venue_list = Venue.objects.filter(venue_Location__icontains=location)
 else:
     category = query[1]
     latest_venue_list = Venue.objects.filter(venue_Location__icontains=location) &\
                     Venue.objects.filter(venue_Category__icontains=category)

 context = {'latest_venue_list': latest_venue_list, 'place_id' : place_id, 'weather_data' : weather_data}
 return render(request, 'travel/results.html', context)

def cinema_locations(request):
    locations = get_cinema_locations()
    for string in locations:
        if not CinemaLocs.objects.filter(location = string.get_text()):
            l = CinemaLocs(location = string.get_text())
            l.save()

    location_list1 = CinemaLocs.objects.order_by('location')[:99]
    location_list2 = CinemaLocs.objects.order_by('location')[100:199]
    location_list3 = CinemaLocs.objects.order_by('location')[200:299]
    location_list4 = CinemaLocs.objects.order_by('location')[300:399]
    location_list5 = CinemaLocs.objects.order_by('location')[400:499]
    location_list6 = CinemaLocs.objects.order_by('location')[500:]

    context = {'location_list1': location_list1, 'location_list2': location_list2, 'location_list3': location_list3,
               'location_list4': location_list4, 'location_list5': location_list5, 'location_list6': location_list6,}
    return render(request, 'travel/locations.html', context)

def cinemas(request):
    result = get_cinemas()
    for i in range(len(result)):
        split = (result[i].strip().splitlines())
        if (len(split) >= 4):
            if not Venue.objects.filter(venue_Name = split[0]):
                c = Venue(venue_Name=split[0], venue_Location=split[1], venue_Category='Cinema',
                          venue_Description=split[2], venue_Site=split[-2], venue_Logo=split[-1],
                          venue_Updated=timezone.now(), venue_Owner=request.user)
                c.save()

    cinema_list = Venue.objects.filter(venue_Category__iexact='cinema')

    context = {'cinema_list': cinema_list}

    return render(request, 'travel/cinemas.html', context)

def detail(request, venue_id):
    response = "You're looking at the results of venue %s"

    venue = Venue.objects.get(id=venue_id)
    place_id = get_place_id(venue.venue_Location)

    context = {'venue': venue, 'place_id': place_id}
    return render(request, 'travel/detail.html', context)
