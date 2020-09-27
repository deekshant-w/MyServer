from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('basicFlow', basicFlow, name='basicFlow'),
    path('preview', previewPage, name='preview'),
    path('videoPreview', videoPreview, name='videoPreview'),
    path('audioPreview', audioPreview, name='audioPreview'),
]
