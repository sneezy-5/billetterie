from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from .models import *



class VehiculeForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = ['nom_vehicule', 'capacite', 'type']


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['adresse', 'nom_destination']


