from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MiFormularioDeCrecionDeUsurios(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repertir Contrseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        