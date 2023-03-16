from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from .models import Account



class UserCreation(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email','phone', 'password1', 'password2']



class ConnexionForm(ModelForm):
    class Meta:
        model = Account
        fields = ["username", "password"]
        widgets = {
            'username': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }