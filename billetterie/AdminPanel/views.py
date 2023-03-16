from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.forms import UserCreation
from .forms import *

# Create your views here.
@login_required(login_url="account:Connexionadmin")
def admin(request):
    return render(request, 'adminPanel/admin.html')


@login_required(login_url="account:Connexionadmin")
def add_agent(request):
    agents = Account.objects.filter(is_staff=True)
    form = VehiculeForm()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.is_staff = True
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'agents':agents,
            'errors' : form.errors.items()
        }
    return render(request, 'adminPanel/dash_html/add_agent.html',context)


@login_required(login_url="account:Connexionadmin")
def ajouter_vehicule(request):

    trajets = Trajet.objects.all()
    vehicules = Vehicule.objects.all()
    form = VehiculeForm()
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        user =  Account.objects.get(id=request.user.id) 
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            #obj.trajet = Trajet.objects.get(pk=request.trajet)
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'trajets':trajets,
            'vehicules': vehicules,
            'errors' : form.errors.items()
        }


    return render(request, 'adminPanel/dash_html/ajouter_vehicule.html', context)


@login_required(login_url="account:Connexionadmin")
def bagage_colis(request):

    colis = Colis.objects.all()
    trajets = Trajet.objects.all()
    vehicules = Vehicule.objects.all()
    form = ColisForm()
    if request.method == 'POST':
        form = ColisForm(request.POST)
        user =  Account.objects.get(id=request.user.id) 
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            #obj.trajet = Trajet.objects.get(pk=request.trajet)
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'trajets':trajets,
            'vehicules': vehicules,
            'colis': colis,
            'errors' : form.errors.items()
        }
    return render(request, 'adminPanel/dash_html/bagage_colis.html',context)


@login_required(login_url="account:Connexionadmin")
def conf_remise(request):
    remise = Remise.objects.all()
    trajets = Trajet.objects.all()
   # vehicules = Vehicule.objects.all()
    form = RemiseForm()
    if request.method == 'POST':
        form = RemiseForm(request.POST)
        user =  Account.objects.get(id=request.user.id) 
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            #obj.trajet = Trajet.objects.get(pk=request.trajet)
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'trajets':trajets,
            'remises': remise,
            'errors' : form.errors.items()
        }
    return render(request, 'adminPanel/dash_html/conf_remise.html',context)


@login_required(login_url="account:Connexionadmin")
def conf_trajet(request):
    trajets = Trajet.objects.all()
    destinations = Destination.objects.all()
    form = TrajetForm()
    if request.method == 'POST':
        form = TrajetForm(request.POST)
        user =  Account.objects.get(id=request.user.id) 
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            # obj.user = request.user
            # obj.destination = Destination.objects.get(pk= request.destination)
            # obj.trajet = Trajet.objects.get(pk=request.trajet)
            # obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    
    context = {
            'form' : form, 
            'trajets':trajets,
            'destinations':destinations,
            'errors' : form.errors.items()
        }
    

    return render(request, 'adminPanel/dash_html/conf_trajet.html',context)


def update_trajet(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    form = TrajetForm(instance=trajet)
    if request.method == 'PUT':
        form = TrajetForm(request.POST, instance=trajet)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.info(request, "Informations enregistrées avec succès!")
    context = {
        'form': form,
        'destinations': Destination.objects.all(),
        'trajet': trajet,
        'errors': form.errors.items()
    }
    return render(request, 'adminPanel/dash_html/conf_trajet.html',context)



def delete_trajet(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    if request.method == 'GET':
        trajet.delete()
        messages.info(request, "Trajet supprimé avec succès!")

    return redirect('nameadmin:conf_trajet')



@login_required(login_url="account:Connexionadmin")
def cree_reservation(request):
    trajets = Trajet.objects.all()
    clients = Account.objects.filter(is_admin=False).filter(is_staff=False)
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            vehicule = Vehicule.objects.filter(trajet=request.POST.get('trajet'))
          
            place =(int(vehicule[0].capacite) +1)- int(vehicule[0].place_restante)
            update_place_restante =int(vehicule[0].place_restante)-1
            # vehicule[0].place_restante=update_place_restante
            # vehicule[0].save()
            # print((int(vehicule[0].capacite) +1)- int(vehicule[0].place_restante))
            # return HttpResponse([vehicule])
            vehic =Vehicule.objects.get(pk=vehicule[0].pk)
            vehic.place_restante= update_place_restante
            vehic.save()
           
            obj = form.save(commit = False)
            obj.client = request.user
            #obj.vehicule = vehicule
            obj.place = place
            # print(obj)
            # return HttpResponse([vehicule])
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'trajets':trajets,
            'clients':clients,
            'errors' : form.errors.items()
        }
    return render(request, 'adminPanel/dash_html/cree_reservation.html', context)


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
    trajets = Trajet.objects.all()
    reservations = Reservations.objects.all()
    if request.method == 'POST':
       query = request.POST.get('trajet')
       print(query)
       reservations = Reservations.objects.filter(trajet=query)
    context = {
            'trajets':trajets,
            'reservations':reservations,
        }
    return render(request, 'adminPanel/dash_html/liste_reservation.html',context)


@login_required(login_url="account:Connexionadmin")
def recherche_trajet(request):
    return render(request, 'adminPanel/dash_html/recherche_trajet.html')
