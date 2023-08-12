from django import forms

class TrekFormulario (forms.Form):
    serie = forms.CharField(max_length=100)
    pilot = forms.IntegerField( max_value=2030)
    temporadas = forms.IntegerField( max_value=10)

class WarsFormulario (forms.Form):
    serie = forms.CharField(required=True, max_length=100)
    año_piloto = forms.IntegerField(required=True, max_value=2030)
    temporadas = forms.IntegerField(required=True, max_value=10)

class OtrasFormulario (forms.Form):
    saga = forms.CharField(max_length=50)
    serie = forms.CharField(required=True, max_length=100)
    año_piloto = forms.IntegerField(required=True, max_value=2030)
    temporadas = forms.IntegerField(required=True, max_value=10)