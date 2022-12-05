from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def reservation(request):
    return render(request, 'htmlPages/reservation.html')


def search(request): 
    return render(request, 'htmlPages/search.html')


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