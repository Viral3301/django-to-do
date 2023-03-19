from .models import Post
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('task_title','task_body','deadline')
        widgets = {
            'task_title' : forms.TextInput(attrs={'class': 'form-title-input', 'placeholder' : 'Название задачи'}),
            'task_body' : forms.Textarea(attrs={'class': 'form-body-input', 'placeholder' : 'Описание'}),
            'deadline' : forms.DateInput(attrs={'class': 'form-deadline-input', 'placeholder' : 'Дата дедлайна : дд.мм.гггг'},format='%d.%m.%Y',)
        }
