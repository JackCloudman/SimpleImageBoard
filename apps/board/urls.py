from . import views
from django.urls import path,include                                                                     
from django.conf.urls import url
from django.contrib.auth.decorators import login_required   
urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/$',views.boardlist),
    path('<board>/',views.showboard,name='showboard'),
    path('<board>/new/',login_required(views.new_post),name='new_post'),
    path('<board>/<pk>/',views.post_detail,name='post_detail'),
]  
