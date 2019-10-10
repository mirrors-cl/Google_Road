from django.urls import path

from . import views

Urlpatterns = [
    path('', views.index, name='index'),
]