from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^email_me/$', views.email_me, name='email_me'),


]
