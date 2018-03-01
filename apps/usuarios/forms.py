from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            ]
        labels = {
            'username':'Nickname',
            'email':'Correo',
            }
