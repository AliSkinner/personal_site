from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.exclude(active=False)
    context = {'hello': 'This is the homepage',
                'items': items,
            }
    print context
    return render(request, "homepage/homepage.html", context)
