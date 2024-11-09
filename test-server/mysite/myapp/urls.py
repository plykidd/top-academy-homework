from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('date/', views.date, name='date'),
    path('table/', views.table, name='table'),
    path('holiday/', views.holiday, name='date-program'),
]
