from django.urls import path 
from .views import index,get_quiz

urlpatterns = [
    path('index', index, name='index'),
    path('api/get-quiz/', get_quiz, name='get_quiz')
]