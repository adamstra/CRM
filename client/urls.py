from django.urls import path
from .views import liste_client, modifier_commande, supprimer_commande

urlpatterns = [
    path('/<str:pk>/', liste_client, name='client'),
    path('modifier/<str:pk>/', modifier_commande, name='update'),
    path('supprimer/<str:pk>/', supprimer_commande, name='delete'),

]
