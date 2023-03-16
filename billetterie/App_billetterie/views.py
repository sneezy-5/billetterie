import datetime
from decimal import Decimal
import time
from django.contrib import messages
from django.shortcuts import render
from AdminPanel.forms import ReservationForm
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from AdminPanel.models import Reservations, Trajet, Vehicule

import json
from datetime import date, datetime

from datetime import datetime, date, time
from decimal import Decimal
from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return list(obj.values())
        elif isinstance(obj, (datetime, date)):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, (time,)):
            return obj.strftime('%H:%M:%S')
        else:
            return super().default(obj)

def datetime_handler(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    elif isinstance(obj, Decimal):
        return str(obj)

    else:
        return None

# Create your views here.
def compte(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def reservation(request):
    trajets = Trajet.objects.all()
    form = ReservationForm()
    code_resevation  = datetime.datetime.now()
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
            #obj.code_reservation = code_resevation
            # print(obj)
            # return HttpResponse([vehicule])
            obj.save()
            messages.info(request, "Information enregistrer avec succes :) ")
    context = {
            'form' : form, 
            'trajets':trajets,
            'errors' : form.errors.items()
        }
    return render(request, 'htmlPages/reservation.html',context)




def search(request): 
    reservations = Reservations.objects.filter(client= request.user)

    reservation_list = serializers.serialize('python', reservations)
    reservation_data = [item['fields'] for item in reservation_list]
    json_data = json.dumps(reservation_data, cls=CustomJSONEncoder)
    # if request.method == 'POST':
    #    query = request.GET.get('trajet')
    #    reservations = Reservations.objects.filter(id=query)
    context = {
            'reservations':reservations,
            'reservationss':json_data
        }


    #print(json_data[0])
    #return HttpResponse(json_data, content_type="application/json")
    return render(request, 'htmlPages/search.html',context)


def paiement(request):
    return render(request, 'htmlPages/paiement.html')


def valider_paiement(request):
    return render(request, 'htmlPages/valider_paiement.html')






def agent(request):
    return render(request, 'agentPanel/agent.html')


def liste_commande(request):
    return render(request, 'agentPanel/liste_commande.html')


def bagage_colis1(request):
    return render(request, 'agentPanel/bagage_colis1.html')


def cree_commande(request):
    return render(request, 'agentPanel/cree_commande.html')


def recherche_trajet1(request):
    return render(request, 'agentPanel/recherche_trajet1.html')


