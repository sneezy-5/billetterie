from django.urls import path
from . import views

app_name = 'appbilletterie'
urlpatterns = [
    path('', views.index, name='index'),
    path('reservation/', views.reservation, name='reservation'),
    path('search/', views.search, name='search'),
    path('paiement/', views.paiement, name='paiement'),
    path('valider_paiement/', views.valider_paiement, name='valider_paiement'),


    path('agent/', views.agent, name='agent'),
    path('liste_commande/', views.liste_commande, name='liste_commande'),
    path('bagage_colis1/', views.bagage_colis1, name='bagage_colis1'),
    path('cree_commande/', views.cree_commande, name='cree_commande'),
    path('recherche_trajet1/', views.recherche_trajet1, name='recherche_trajet1'),

]