from django.shortcuts import render
from app_1.models import Topic, Emtry
from django.shortcuts import render, redirect
from app_1.forms import TopicForm, EmtryForm


def index(request):
    return render(request, 'app_1/index.html')


def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'app_1/topics.html', context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = Emtry.objects.filter(topic_id=topic_id)
    context = {'topic': topic, "entries": entries}
    return render(request, 'app_1/topic.html', context)


def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_1:topics')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'app_1/new_topic.html', context)


def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""
    #topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EmtryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EmtryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save()
            new_entry.topic_id = topic_id
            new_entry.save()
            return redirect('app_1:topic', topic_id=topic_id)
    # Вывести пустую или недействительную форму.
    context = {'topic': topic, 'form': form}
    return render(request, 'app_1/new_entry.html', context)


