from django.urls import path
from . import views
urlpatterns=[
    path('a1/',views.detail,name='detail'),
    path('',views.home,name='home'),
    path('index1/',views.index,name='index'),
 ]