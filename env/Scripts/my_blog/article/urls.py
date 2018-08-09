from django.urls import path
from . import views
from article.views import RSSFeed
urlpatterns=[
    path('<int:id>/',views.detail,name='detail'),
    path('',views.home,name='home'),
    path('index1/',views.index,name='index'),
    path('tag<str:tag>/',views.search_tag,name='search_tag'),
    path('search/',views.blog_search,name='blog_search'),
    path('archives/',views.archives,name='archives'),
    path('feed/',RSSFeed,name='RSS'),
 ]