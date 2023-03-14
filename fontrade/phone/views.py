from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

main = ['Контакты', 'Вакансии', 'Отзывы', 'Адрес']


def index(request):
    posts = Phone.objects.all()
    return render(request, 'phone/index.html', {'posts': posts, 'main': main, 'title': 'Главная страница'})


def categories(request):
    if request.GET:
        return redirect('/', permanent=True)
    return render(request, 'phone/about.html', {'main': main, 'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def archive(request, number):
    print(request.GET)
    return HttpResponse(f'<h1>АРХИВ {number}</h1>')
