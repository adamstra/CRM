from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client
from commande.forms import CommandeForm
from commande.filtres import CommandeFiltre
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='acces')
def liste_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()

    myFilter = CommandeFiltre(request.GET, queryset=commande)
    commande = myFilter.qs

    context = {'client': client, 'commande': commande,
               'commande_total': commande_total, 'myFilter': myFilter}
    return render(request, 'client/list_client.html', context)


@login_required(login_url='acces')
def modifier_commande(request, pk):
    client = Client.objects.get(id=pk)
    form = CommandeForm(instance=client)

    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


@login_required(login_url='acces')
def supprimer_commande(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')

    context = {'item': client}
    return render(request, 'commande/supprimer_commande.html', context)
