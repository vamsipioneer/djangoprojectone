
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("HEllo VAMSI....")

def login(request):
    return HttpResponse("Hello login.....")

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'login.html', context=None)

class TestView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'base_generic.html', context=None)


class AboutPageView(TemplateView):
	template_name = "userlogin.html"
