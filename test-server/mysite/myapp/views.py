from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def date(request):
    date_time = datetime.datetime.now()
    return HttpResponse(f'Текущее время: {date_time}')


def table(request):
    b = ''
    for number in range(1, 11):
        b += f'{5}*{number} = {5 * number}<br>'
    return HttpResponse(b)


def holiday(request):
    today = datetime.date.today()
    NY = datetime.date(today.year, 1, 1)
    holiday = NY + datetime.timedelta(days=255)
    return HttpResponse(f'Дата дня програмиста в этом году: {holiday}')
