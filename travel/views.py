from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    a = 'vladik'
    return render(request, 'home.html', {'a': a})

def about(request):
    return render(request, 'about.html')