from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from myapp1.models import WeatherApp


# Create your views here.
def view_weather(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    xy = 1000
    data["time_of_day"] = time
    data['xy'] = xy

    return render(request, "weather.html", context=data)


def view_city(request):
    return render(request, "weather1.html")
