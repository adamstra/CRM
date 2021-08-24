from django.urls import path
from .views import list_commande, ajouter_commande, modifier_commande, supprimer_commande

urlpatterns = [
    path('', list_commande, name='commande'),
    path('ajouter/', ajouter_commande, name='ajouter'),
    path('modifier/<str:pk>/', modifier_commande, name='update'),
    path('supprimer/<str:pk>/', supprimer_commande, name='delete'),
]
