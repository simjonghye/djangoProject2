from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from . import views
from django.http import HttpResponse

from django.views.generic.list import ListView
# 템플릿 : 화면을 꾸며주는 역할

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return HttpResponse()
    # return render(request, 'first/question_list.html', context)

def url_view(request):
    print('url_view()')
    data={'code':'001', 'msg':'OK'}
    return HttpResponse('<h1>url_view</h1>')

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method=='GET':
        print(f'request.GET: {request.GET}')
    elif request.method=='POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'first/view.html')

# class ClassView(ListView):
#     model = First
#     template_name = 'cbv_view.html'