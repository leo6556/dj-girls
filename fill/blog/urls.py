from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/<pk>/', detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    path('edit/', post_edit, name='post_edit')
]
