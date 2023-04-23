from django.conf import settings
import os

from django.urls import path
from . import views
from .load_images import load_images_from_raw_folder

urlpatterns = [
    path('', views.home, name='home'),
]


RAW_IMAGES_FOLDER = os.path.join(settings.BASE_DIR, 'media', 'raw')
load_images_from_raw_folder(RAW_IMAGES_FOLDER)