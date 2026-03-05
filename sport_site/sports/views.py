from django.shortcuts import render

def index(request):
    return render(request, 'sports/index.html', {'title': 'Головна'})

def football(request):
    return render(request, 'sports/football.html', {'title': 'Футбол'})

def hockey(request):
    return render(request, 'sports/hockey.html', {'title': 'Хокей'})

def basketball(request):
    return render(request, 'sports/basketball.html', {'title': 'Баскетбол'})
