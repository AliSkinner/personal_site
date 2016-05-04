from django.conf.urls import url
from homepage.views import ProjectListView

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^email_me/$', views.email_me, name='email_me'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='projects'),

]
