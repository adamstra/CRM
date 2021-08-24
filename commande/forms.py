from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):
    # models = Commande

    class Meta:
        model = Commande
        fields = '__all__'
        # widgets = {
        #     'client': forms.TextInput(attrs={'class': 'form-control'}),
        #     'produit': forms.TextInput(attrs={'class': 'form-control'}),
        #     'status': forms.TextInput(attrs={'class': 'form-control'})
        # }
