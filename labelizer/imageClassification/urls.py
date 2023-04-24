from django.conf import settings
import os

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

