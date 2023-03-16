from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from .models import *



class VehiculeForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'nom_vehicule', 'capacite','type','trajet']


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['adresse', 'nom_destination']

class TrajetForm(ModelForm):
    class Meta:
        model = Trajet
        fields = ['code_trajet', 'lieu_depart','lieu_arrivee','heure_debut','heure_fin','prix']


class RemiseForm(ModelForm):
    class Meta:
        model = Remise
        fields = ['code_remise','date_debut','date_fin','montant','statut_remise', 'trajet']


class ColisForm(ModelForm):
    class Meta:
        model = Colis
        fields = ['code_colis','trajet','date_depart','nom_expediteur','nom_destinataire','status','type','quantite','poids', 'prix_unitaire','vehicule']

class ReservationForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ['trajet', 'date_depat','heure_depat']

