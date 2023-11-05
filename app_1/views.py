from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'app_1/index.html')


def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'app_1/topics.html', context)
