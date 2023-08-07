from django import forms

class TrekFormulario (forms.Form):
    titulo = forms.CharField(max_length=100)
    año_piloto = forms.IntegerField(required=True, max_value=2030)
    temporadas = forms.IntegerField(required=True, max_value=10)

class WarsFormulario (forms.Form):
    titulo = forms.CharField(max_length=100)
    año_piloto = forms.IntegerField(required=True, max_value=2030)
    temporadas = forms.IntegerField(required=True, max_value=10)

class OtrasFormulario (forms.Form):
    saga = forms.CharField(required=False, max_length=50)
    titulo = forms.CharField(max_length=100)
    año_piloto = forms.IntegerField(required=True, max_value=2030)
    temporadas = forms.IntegerField(required=True, max_value=10)