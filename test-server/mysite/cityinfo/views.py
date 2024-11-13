from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return HttpResponse("Главная страница г. Красноярска")


def news_page(request):
    return HttpResponse("Новости г. Красноярска")


def management_page(request):
    return HttpResponse("Руководство по г. Красноярск")


def facts_page(request):
    return HttpResponse("Факты о г. Красноярске")


def contact_page(request):
    return HttpResponse('Номера телефонов городских служб')
