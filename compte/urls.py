from django.urls import path
from .views import inscriptionPage, accesPage, logoutUser

urlpatterns = [
    path('inscription/', inscriptionPage, name='inscription'),
    path('acces/', accesPage, name='acces'),
    path('quitter/', logoutUser, name='quitter'),
]
