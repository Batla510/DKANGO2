from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    text = f' host: {host},browser {user_agent},path {path}'
    return HttpResponse(text, headers={'SecretCode':'12312123'})

def user(request,name='Noname',age=0):
    return HttpResponse(f'User:{name},His age is {age}')