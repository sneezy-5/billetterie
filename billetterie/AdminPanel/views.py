from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url="account:Connexionadmin")
def admin(request):
    return render(request, 'adminPanel/admin.html')


@login_required(login_url="account:Connexionadmin")
def add_agent(request):
    return render(request, 'adminPanel/dash_html/add_agent.html')


@login_required(login_url="account:Connexionadmin")
def ajouter_vehicule(request):

    destinations = Destination.objects.all()
    trajets = Trajet.objects.all()
    form = VehiculeForm()
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        user =  Account.objects.get(id=request.user.id) 
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.destination = Destination.objects.get(pk= request.destination)
            obj.trajet = Trajet.objects.get(pk=request.trajet)
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'destinations':destinations,
            'trajets':trajets,
            'errors' : form.errors.items()
        }


    return render(request, 'adminPanel/dash_html/ajouter_vehicule.html', context)


@login_required(login_url="account:Connexionadmin")
def bagage_colis(request):
    return render(request, 'adminPanel/dash_html/bagage_colis.html')


@login_required(login_url="account:Connexionadmin")
def conf_remise(request):
    return render(request, 'adminPanel/dash_html/conf_remise.html')


@login_required(login_url="account:Connexionadmin")
def conf_trajet(request):
    return render(request, 'adminPanel/dash_html/conf_trajet.html')


@login_required(login_url="account:Connexionadmin")
def cree_reservation(request):
    return render(request, 'adminPanel/dash_html/cree_reservation.html')


@login_required(login_url="account:Connexionadmin")
def cree_destination(request):
    destinations = Destination.objects.all()
    form = DestinationForm()
    if request.method == 'POST':
        form = DestinationForm(request.POST)

        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
             'destinations':destinations,
            'errors' : form.errors.items()
        }


    return render(request, 'adminPanel/dash_html/cree_destination.html',context)


@login_required(login_url="account:Connexionadmin")
def rapport_activite(request):
    return render(request, 'adminPanel/dash_html/rapport_activite.html')


@login_required(login_url="account:Connexionadmin")
def rapport_agent(request):
    return render(request, 'adminPanel/dash_html/rapport_agent.html')


@login_required(login_url="account:Connexionadmin")
def liste_passager(request):
    return render(request, 'adminPanel/dash_html/liste_passager.html')


@login_required(login_url="account:Connexionadmin")
def liste_reservation(request):
    return render(request, 'adminPanel/dash_html/liste_reservation.html')


@login_required(login_url="account:Connexionadmin")
def recherche_trajet(request):
    return render(request, 'adminPanel/dash_html/recherche_trajet.html')
