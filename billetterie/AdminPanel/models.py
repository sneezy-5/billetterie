from django.db import models
from account.models import Account

# Create your models here.

class Trajet(models.Model):
    code_trajet = models.IntegerField(max_length=50)
    lieu_depart = models.CharField(max_length=100)
    lieu_arrivee = models.CharField(max_length=100)
    heure_debut	= models.TimeField()
    heure_fin = models.TimeField()
    prix = models.IntegerField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(Account, verbose_name='reservation')





class Destination(models.Model):
    adresse = models.CharField(max_length=100)
    nom_destination = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE )




class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=60, default='')
    nom_vehicule = models.CharField(max_length=50, default='')
    capacite = models.IntegerField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, default='')
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, default='')
    
    



class Remise(models.Model):
    code_remise = models.IntegerField(max_length=60)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant	= models.IntegerField(max_length=100)
    statut_remise = models.BooleanField()
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey( Account, on_delete=models.CASCADE)
    trajet = models.OneToOneField( Trajet, on_delete=models.CASCADE)



class Cycle_trajet(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()

    user = models.ForeignKey( Account, on_delete=models.CASCADE)
    vehicule = models.ForeignKey( Vehicule, on_delete=models.CASCADE)




class colis(models.Model):
    code_colis = models.CharField(max_length=60)
    lieu_depart = models.CharField(max_length=100)
    lieu_arrivee = models.CharField(max_length=100)
    date_depart = models.DateField()
    nom_expediteur	= models.CharField(max_length=100)
    nom_destinataire = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantite = models.IntegerField(max_length=100)
    poids = models.IntegerField(max_length=100)
    prix_unitaire = models.IntegerField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey( Account, on_delete=models.CASCADE) 
    vehicule = models.ForeignKey( Vehicule, on_delete=models.CASCADE)
