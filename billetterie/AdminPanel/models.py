import datetime
from django.db import models
from account.models import Account

# Create your models here.

class Trajet(models.Model):
    code_trajet = models.CharField(max_length=50)
    lieu_depart = models.CharField(max_length=100, default="")
    lieu_arrivee = models.CharField(max_length=100, default="")
    heure_debut	= models.TimeField()
    heure_fin = models.TimeField()
    prix = models.IntegerField(max_length=100)
   # vehicule = models.ManyToManyField('Vehicule')
    date_enregistrement = models.DateTimeField(auto_now=True)    
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default="")





class Destination(models.Model):
    adresse = models.CharField(max_length=100)
    nom_destination = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE )




class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=60, default='')
    nom_vehicule = models.CharField(max_length=50, default='')
    capacite = models.IntegerField( default='')
    place_restante = models.IntegerField( default=80,null=True)
    type = models.CharField(max_length=100, default='')
    date_enregistrement = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    #destination = models.ForeignKey(Destination, on_delete=models.CASCADE, default='')
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
    #vehicule = models.OneToOneField( Vehicule, on_delete=models.CASCADE, default="")


# class Cycle_trajet(models.Model):
#     date_debut = models.DateField()
#     date_fin = models.DateField()

#     user = models.ForeignKey( Account, on_delete=models.CASCADE)
#     vehicule = models.ForeignKey( Vehicule, on_delete=models.CASCADE)




class Colis(models.Model):
    code_colis = models.CharField(max_length=60)
    trajet = models.ForeignKey(Trajet,on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=100, default="")
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


class Reservations(models.Model):
    #code_reservation = models.CharField(max_length=10,default="",unique=True)
    client = models.ForeignKey(Account,on_delete=models.CASCADE,default="")
    status = models.BooleanField(default=1)
    trajet = models.ForeignKey(Trajet,on_delete=models.CASCADE)
    date_depat = models.DateTimeField()
    heure_depat = models.TimeField(default=datetime.datetime.now())
    place = models.IntegerField(default=1)
    #vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now=True)
    #models.ManyToManyField(Account, verbose_name='reservation')