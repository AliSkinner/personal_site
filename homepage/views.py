from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Project
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

class HomePageView(TemplateView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class ContactPageView(TemplateView):
    template_name = "homepage/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        return context

def email_me(request):
    subject = 'Email Contact from AliSkinner.com'
    body = request.POST['email-me-message']
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ["awskinner26@gmail.com"])
    return HttpResponse('success')

class AboutPageView(TemplateView):
    template_name = "homepage/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        return context

class ProjectListView(ListView):
    # model = Project
    context_object_name = 'project_list'
    queryset = Project.objects.all().order_by('display_order')
    template_name = "homepage/projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        return context
