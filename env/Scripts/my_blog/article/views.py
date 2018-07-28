# coding:utf-8
from django.shortcuts import render
from article.models import Article
# Create your views here.
from django.http import HttpResponse

def home(request):
	post_list=Article.objects.all()
	return render(request,'article/home.html',{'post_list':post_list})

def detail(request):
    return HttpResponse("you are looking at my_args ")

def index(request):
 	return render(request,'article/index.html')

