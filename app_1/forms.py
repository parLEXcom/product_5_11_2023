from django import forms
from app_1.models import Topic, Emtry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Писать сюда!'}


class EmtryForm(forms.ModelForm):
    class Meta:
        model = Emtry
        fields = ['text']
        labels = {'text': 'Создать статью:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
