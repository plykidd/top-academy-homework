from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit, name='edit_task'),
    path('completed/<id>/', views.completed_task, name='completed_task'),
]