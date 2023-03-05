from django.urls import path

from .views import *

urlpatterns = [
    path('cats/', index),
    path('dogs/', categories),
    path('archive/<path:number>/', archive)
]
