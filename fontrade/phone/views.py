from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Phone.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               }
    return render(request, 'phone/index.html', context=context)


def about(request):
    if request.GET:
        return redirect('/', permanent=True)
    context = {'menu': menu,
               'title': 'О сайте',
               }
    return render(request, 'phone/about.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена!')


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
