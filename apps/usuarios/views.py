from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroForm,UserForm,ProfileForm
from django.shortcuts import render,redirect
class RegistroUsuarios(CreateView):
    model = User
    template_name = "usuarios/registrar.html"
    form_class = RegistroForm
    @property
    def success_url(self):
        return '/'
def profile(request):
    return render(request,'profile.html',{})
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            if 'userpic' in request.FILES:
                print("Foto!")
                p = profile_form.save(commit=False)
                p.picture = request.FILES['userpic']
                p.save()
            user_form.save()
            profile_form.save()
            return redirect('/profile/')
        else:print("NO se pudo guardar")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/editprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
# Create your views here.
