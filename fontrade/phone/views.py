from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

main = ['Контакты', 'Вакансии', 'Отзывы', 'Адрес']


def index(request):
    posts = Phone.objects.all()
    context = {'posts': posts,
               'main': main,
               'title': 'Главная страница',
    }
    return render(request, 'phone/index.html', context=context)


def about(request):
    if request.GET:
        return redirect('/', permanent=True)
    context = {'main': main,
               'title': 'О сайте',
    }
    return render(request, 'phone/about.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена!')
