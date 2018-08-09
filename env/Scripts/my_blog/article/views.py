# coding:utf-8
from django.shortcuts import render,redirect
from article.models import Article
from datetime import datetime
from django.contrib.syndication.views import Feed
# Create your views here.
from django.http import HttpResponse,Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def home(request):
	post=Article.objects.all()
	paginator=Paginator(post,2)
	page=request.GET.get('page')
	try:
		post_list=paginator.page(page)
	except PageNotAnInteger:
		post_list=paginator.page(1)
	except EmptyPage:
		post_list=paginator.paginator(paginator.num_pages)
	return render(request,'article/home.html',{'post_list':post_list})
	

def detail(request,id):
	try:
		post=Article.objects.get(id=str(id))
	except:
		return HttpResponse("hello")
	return render(request,'article/post.html',{'post':post})

def index(request):
 	return render(request,'article/index.html')

def search_tag(request,tag):
 	try:
 		post_list=Article.objects.filter(category__iexact=tag)
 		return render(request,'article/tag.html',{'post_list':post_list})
 	except Article.DoesNotExist:
 		raise Http404


def blog_search(request):
	if 'sss' in request.GET:
	#return HttpResponse("wwwww")
		
		s=request.GET['sss']
		if not s:
			return render(request,'article/archives.html',{'post_list':post_list,'error':True})
		else:
			post_list=Article.objects.filter(title__icontains=s)
			if len(post_list)==0:
				return render(request,'article/archives.html',{'post_list':post_list,'error':True})
			else:
				return render(request,'article/archives.html',{'post_list':post_list,'error':False})
			#return redirect('/')	
	else:
		return HttpResponse(request.GET.get('sss'))


def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})

class RSSFeed(Feed):
	title="RSS feed-aritcle"
	template_name="article/post.html"
	desrciption="RSS feed - blog posts"
    
	def items(self):
		return Article.objects.order_by('-date_time')

	def item_title(self,item):
		return item.title

	def item_pubdate(self,item):
		return item.add_date

	def item_description(self,item):
		return item.content
