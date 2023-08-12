from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    apellido = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(required=True)

class ConsultaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    email = forms.EmailField(required=True)
    detalle = forms.CharField(widget=forms.Textarea)