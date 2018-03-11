from . import views
from django.urls import path,include                                                                     
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.index),
    path('<str:board>/',views.showboard,name='showboard'),
]  
