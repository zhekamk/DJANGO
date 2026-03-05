from django.shortcuts import render

def home(request):
    return render(request, 'city_info/base.html')

def news(request):
    return render(request, 'city_info/news.html')

def management(request):
    return render(request, 'city_info/management.html')

def facts(request):
    return render(request, 'city_info/facts.html')

def contacts(request):
    return render(request, 'city_info/contacts.html')

def history(request):
    return render(request, 'city_info/history.html')

def history_people(request):
    return render(request, 'city_info/history_people.html')

def history_photos(request):
    return render(request, 'city_info/history_photos.html')