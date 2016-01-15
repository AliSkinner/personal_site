from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def home(request):
    # to change
    context = {
                'portrait_pic': 'portrait_pic',
                'tag_line': 'tag_line',
            }

    return render(request, "homepage/homepage.html", context)
