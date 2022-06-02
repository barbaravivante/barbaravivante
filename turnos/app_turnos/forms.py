from django import forms


class Alta_turno(forms.Form):

    nombre = forms.CharField(max_length=40)
    domicilio = forms.CharField(max_length=40)

class Alta_cliente(forms.Form):

    nombre = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    telefono= forms.IntegerField()
    domicilio= forms.CharField(max_length=40)
    email = forms.CharField(max_length=20)

class Alta_profesionales(forms.Form):

    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    turno= forms.CharField(max_length=40)     

