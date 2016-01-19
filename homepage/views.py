from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def home(request):
    # to change
    context = {
                'portrait_pic': 'portrait_pic',
                'tag_line': 'tag_line',
            }
    return render(request, "homepage/homepage.html", context)

def contact(request):
    context = {}
    return render(request, "homepage/contact.html", context)

def email_me(request):

    subject = 'Email Contact from AliSkinner.com'
    body = request.POST['email-me-message']
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ["awskinner26@gmail.com"])
        return HttpResponse('success')
    except Exception as e:
        return HttpResponse('fail')
