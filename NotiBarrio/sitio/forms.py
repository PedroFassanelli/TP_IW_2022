from django import forms
from sitio.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class FromCrearUsuario(forms.Form):
    first_name = forms.CharField(max_length= 15, label='Nombre')
    last_name = forms.CharField(max_length= 25, label='Apellido')
    email = forms.EmailField(max_length= 50, label='Correo electronico')
    location = forms.CharField(max_length=50, label='Barrio')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar contraseña')
    born = forms.DateField

    '''Validaciones'''
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if len(password) < 8:
            raise forms.ValidationError('Las contraseñas no pueden tener menos de 8 caracteres.')
        return password2
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude().filter(email=email).exists():
            raise forms.ValidationError('El Email elegido ya esta en uso.')
        return email

class FromLogin(forms.Form):
    email = forms.EmailField(max_length= 50, label='Correo electronico')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')


'''class FromNuevaPublicacion(forms.From):
    pass'''