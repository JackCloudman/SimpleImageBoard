from django.conf.urls import url
from apps.usuarios.views import RegistroUsuarios
from django.contrib.auth.views import login,logout                                                                                      
from django.contrib.auth.decorators import login_required   
from . import views
urlpatterns = [
    url(r'^register/$',RegistroUsuarios.as_view()),
    url(r'^login/$',login,{'template_name':'login.html'}),
    url(r'^logout/$', logout, {'next_page':'/'}),
    url(r'^profile/edit/$',views.update_profile,name='edit_profile'), 
    url(r'^profile/$',login_required(views.profile)), 
]
