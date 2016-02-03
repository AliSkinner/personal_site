from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template import loader

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hello'] = 'world'
        return context

#
# def home(request):
#     # to change
#     context = {
#                 'portrait_pic': 'portrait_pic',
#                 'tag_line': 'tag_line',
#             }
#     template = loader.get_template("homepage/homepage.html")
#
#     return HttpResponse(template.render(context, request))

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
