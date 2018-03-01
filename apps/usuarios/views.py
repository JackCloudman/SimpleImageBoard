from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroForm
class RegistroUsuarios(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistroForm
    @property
    def success_url(self):
        return '/'
# Create your views here.
