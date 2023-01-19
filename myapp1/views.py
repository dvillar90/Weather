from django.shortcuts import render

# Create your views here.
def view_weather(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    xy = 1000
    data["time_of_day"] = time
    data['xy'] = xy

    return render(request, "weather.html", context=data)
