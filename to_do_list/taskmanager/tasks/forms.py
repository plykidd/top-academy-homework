from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput
from django.forms.widgets import CheckboxSelectMultiple
from django import forms


class TaskForm(ModelForm):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': ''}))
    description = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = '__all__'

        # widgets = {
        #     'title': TextInput(attrs={
        #         'placeholder': 'Задача'
        #     }),
        #     'description': TextInput(attrs={
        #         'placeholder': 'Описание'
        #     }),
        #     'is_completed': forms.RadioSelect(attrs={
        #         'placeholder': 'Статус'
        #     }),
        #         'created_at': DateTimeInput(attrs={
        #         'placeholder' : 'Статус'
        #     })
        # }
