from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('My own page!')


def categories(request):
    if request.GET:
        return redirect('/', permanent=True)
    return HttpResponse('<h1>Hello world!</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def archive(request, number):
    print(request.GET)
    return HttpResponse(f'<h1>АРХИВ {number}</h1>')
