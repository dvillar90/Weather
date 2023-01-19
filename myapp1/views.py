from django.shortcuts import render

# Create your views here.
def view_weather(request):
    data = dict()
    w1 = WeatherApp(city="New York", country="USA", weather=10.0)
    c_list= w1
    data['weather']=c_list

    return render(request, "weather.html", context=data)
