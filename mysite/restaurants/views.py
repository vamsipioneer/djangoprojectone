import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    num = random.randint(0,10000000)
    context = {"html_var" : "application has",
                "num":num,
                 "bool_item":True,
                 "some_list" : [10,20,304, 45,3344,45454,65534]}
    return render(request, "home.html",context)

def about(request):
    context = {}
    return render(request, "about.html",context)

def contact(request):
    context = {}
    return render(request, "contact.html",context)
