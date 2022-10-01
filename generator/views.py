from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-<>,*~`'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def div(a,b):
    d = a // b
    return d

def sub(a,b):
    s = a-b
    retunr s

def sum(a,b):
    sum = a+b
    return sum

def mul(a,b):
    m = a//b
    return m
