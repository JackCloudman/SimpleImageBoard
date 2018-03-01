from django.conf.urls import url
from apps.usuarios.views import RegistroUsuarios
urlpatterns = [
    url(r'',RegistroUsuarios.as_view())
]
