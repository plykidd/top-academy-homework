from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def tasks(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': task} )


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/')

    context = {'form': TaskForm()}

    return render(request, "add.html", context)

# def edit_task(request, id):
#     tasks = get_object_or_404(Task, id=id)
#     if request.method == 'POST':
#         tasks.name = request.POST['name']
#         tasks.description = request.POST['description']
#         tasks.is_completed = request.POST['is_completed']
#         tasks.created = request.POST['created']
#         tasks.save()
#         return redirect('tasks')
#     return render(request, 'edit_task.html', {'tasks': tasks})
#
# def completed_task(request, id):
#     task = get_object_or_404(Task, id=id)
