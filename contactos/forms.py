#encoding:utf-8
from django.forms import ModelForm
from contactos.models import Contacto
#from django import forms

class ContactoForm(ModelForm):
	class Meta:
		model = Contacto
