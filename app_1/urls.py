"""Схемы для модели app_1"""

from django.urls import path
from . import views

app_name = 'app_1'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name='topics'),
]