from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random 
# Create your views here.

def index(request):
    return render(request, 'index.html')


def get_quiz(reguest):
    try:
        question_objs = list(Question.objects.all())
        data=[]
        random.shuffle((question_objs))
        print(question_objs)
        for question_obj in question_objs:
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
                })
        payload = {'status' : True, 'data':data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse('Что-то пошло не так')