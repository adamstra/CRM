from django.contrib.auth import authenticate, logout
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreeUtilisateur
from django.contrib import messages

# Create your views here.
def inscriptionPage(request):
  form = CreeUtilisateur()
  if request.method == 'POST':
    form = CreeUtilisateur(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request,"Compte cree avec succes pour "+user)
      return redirect('acces')
  context = {'form':form}
  return render(request, 'compte/inscription.html',context)


def accesPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request,'No username or password')
    
  context = {}
  return render(request, 'compte/acces.html')

def logoutUser(request):
  logout(request)
  return redirect('acces')