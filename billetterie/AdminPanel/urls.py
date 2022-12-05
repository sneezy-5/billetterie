from django.urls import path
from . import views

app_name = 'nameadmin'
urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('admin/add_agent/', views.add_agent, name='add_agent'),
    path('admin/ajouter_vehicule/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('admin/bagage_colis/', views.bagage_colis, name='bagage_colis'),
    path('admin/conf_remise/', views.conf_remise, name='conf_remise'),
    path('admin/conf_trajet/', views.conf_trajet, name='conf_trajet'),
    path('admin/cree_reservation/', views.cree_reservation, name='cree_reservation'),
    path('admin/cree_destination/', views.cree_destination, name='cree_destination'),
    path('admin/liste_passager/', views.liste_passager, name='liste_passager'),
    path('admin/liste_reservation/', views.liste_reservation, name='liste_reservation'),
    path('admin/recherche_trajet/', views.recherche_trajet, name='recherche_trajet'),
    path('admin/rapport_activite/', views.rapport_activite, name='rapport_activite'),
    path('admin/rapport_agent/', views.rapport_agent, name='rapport_agent'),
]