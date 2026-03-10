from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index.html')

def demo(request):
    return render(request, 'webapp/demo.html')

def archives(request):
    return render(request, 'webapp/archives.html')

def page(request):
    return render(request, 'webapp/page.html')

def blog (request):
    return render(request, 'webapp/blog.html')

def single (request):
    return render(request, 'webapp/single.html')





