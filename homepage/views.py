from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {'hello': 'This is the homepage'}
    return render(request, "homepage/homepage.html", context)
