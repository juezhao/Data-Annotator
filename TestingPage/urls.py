from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestingPage, name='TestingPage'),
]
