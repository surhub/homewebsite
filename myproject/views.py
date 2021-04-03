from django.http import HttpResponse
from django.shortcuts import render


# creating views
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def work(request):
    return render(request, 'work.html')
