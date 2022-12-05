from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('Inscription/', views.Inscription, name='Inscription'),
    path('Connexion', views.Connexion, name='connexion'),
    path('admin/connexion', views.Connexionadmin, name='Connexionadmin'),
    path('logoutUser', views.logoutUser, name='logoutUser'),

]