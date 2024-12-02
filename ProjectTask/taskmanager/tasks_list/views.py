from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list/tsk_html.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/')

    context = {'form': TaskForm()}

    return render(request, "tasks_list/add_task.html", context)


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
def completed_task(request, task_id):
    todo = Task.objects.get(pk=task_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def edit(request, id):
    edit_task = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        context = {'form': TaskForm(instance=edit_task), 'id':id}
        return render(request, 'edit.html',context)
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=edit_task)
        form.save()
        return redirect('index')
