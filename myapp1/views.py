from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def view_weather(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    xy = 1000
    data["time_of_day"] = time
    data['xy'] = xy

    return render(request, "weather.html", context=data)

def city(request):
    data = dict()
    w1 = WeatherApp(city="New York", country="USA", weather=10.0)
    w2 = WeatherApp(city="London", country="England", weather=15.0)
    c_list = WeatherApp.objects.all()
    data['weather'] = c_list
    return render(request, "weather1.html", context=data)
