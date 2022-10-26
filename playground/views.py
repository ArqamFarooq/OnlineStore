from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response

def my_world(request):
  return render(request, 'myworld.html')

def say_hello(request):
  return render(request, 'hello.html', {'name': 'Arqam  '})

