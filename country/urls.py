from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contacts', views.contacts, name = 'contacts'),
    path('services', views.services, name = 'services')
]
