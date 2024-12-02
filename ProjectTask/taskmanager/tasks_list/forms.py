from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, CheckboxInput
from django.forms.widgets import CheckboxSelectMultiple
from django import forms


class TaskForm(ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': ''}))
    description = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Задача'
            }),
            'description': TextInput(attrs={
                'placeholder': 'Описание'
            }),
            'completed': CheckboxInput(attrs={
                'class': 'required checkbox form-control'
            }),
        #         'created_at': DateTimeInput(attrs={
        #         'placeholder' : 'Статус'
        #     })
        }
