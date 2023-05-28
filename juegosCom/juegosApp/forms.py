from django import forms

class juegoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    descripcion = forms.CharField(required=True, max_length=500)
    genero = forms.CharField(required=True, max_length=40)
    lanzamiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    clasificacion = forms.IntegerField(required=True, max_value=18)
    costo = forms.IntegerField(required=True, max_value=30000)