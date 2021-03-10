from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
   # return HttpResponse('our first django page')
   return render(request, 'generator/home.html')

def password(request):
       # return HttpResponse('our first django page')
   myPassword=''
   characters= list('abcdefghijklmnopqrstuvwxyz')
   length =int(request.GET.get('length'));
   if request.GET.get('uppercase'):
          characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
   if request.GET.get('numbers'):
          characters.extend(list("0123456789"))
   if request.GET.get('specials'):
          characters.extend(list("~!@#$%^&*()_+{}[]:<>?"))

   for x in range(length):
          myPassword += random.choice(characters)
   return render(request, 'generator/password.html', {"password":myPassword})

def about(request):
   return render(request, 'generator/about.html')
