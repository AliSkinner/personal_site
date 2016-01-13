from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.exclude(active=False)
    context = {
                'items': items,
            }
    return render(request, "homepage/homepage.html", context)
