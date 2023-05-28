from django import forms

class juegoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    descripcion = forms.CharField(required=True, max_length=500)
    genero = forms.CharField(required=True, max_length=40)
    lanzamiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    clasificacion = forms.IntegerField(required=True)
    costo = forms.IntegerField(required=True)