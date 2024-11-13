from django.urls import path
from . import views





urlpatterns = [
    path('', views.main_page, name='main'),
    path('news/', views.news_page, name='news'),
    path('management/', views.management_page, name='management'),
    path('facts/', views.facts_page, name='facts'),
    path('contact_page/', views.contact_page, name='contact_page'),
]
