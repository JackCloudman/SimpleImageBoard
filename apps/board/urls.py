from . import views
from django.urls import path,include                                                                     
from django.conf.urls import url
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$',login,{'template_name':'login.html'}),
    url(r'^logout/$', logout, {'next_page':'/'}),
    url(r'^profile/$',login_required(views.profile)),
]  
