# coding:utf-8
from django.shortcuts import render
from article.models import Article
from datetime import datetime
# Create your views here.
from django.http import HttpResponse,Http404

def home(request):
	post_list=Article.objects.all()
	return render(request,'article/home.html',{'post_list':post_list})

def detail(request,id):
	try:
		post=Article.objects.get(id=str(id))
	except:
		return HttpResponse("hello")
	return render(request,'article/post.html',{'post':post})

def index(request):
 	return render(request,'article/index.html')

