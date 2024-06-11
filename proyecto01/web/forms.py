# forms.py
from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    fecha = forms.DateTimeField(
        label='Fecha de compra',  # Cambia el label del campo
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Venta
        fields = ['cancha', 'cliente', 'fecha']
