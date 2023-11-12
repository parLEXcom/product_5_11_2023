"""Схемы для модели app_1"""

from django.urls import path
from . import views

app_name = 'app_1'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # новый топик
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]