from django.shortcuts import render, redirect

from .models import Task


def tasks(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task': task})


