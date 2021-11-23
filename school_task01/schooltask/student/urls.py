from django.urls import path

from .views import *

irlpatterns = [
    path('', HomePageView.as_view(), name='home')
]    