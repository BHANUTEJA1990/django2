
from django.contrib import admin
from django.urls import path, re_path,include
from . import views

urlpatterns = [
    path('media/<action>', views.media, name='media'),
]
