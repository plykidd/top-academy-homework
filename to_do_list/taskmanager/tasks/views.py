from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task



def tasks(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        is_completed = request.POST['is_completed']
        created = request.POST['created']
        Task.objects.create(name=name, description=description, is_completed=is_completed, created=created)
        return redirect('tasks')
    return render(request, 'add.html')