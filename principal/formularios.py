from django import forms
from principal.models import *
from django.contrib.admin import widgets   

class loginForms( forms.Form ):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class cxpForms( forms.ModelForm ):	
	class Meta:
		model = cxp
		exclude = ('monto_total',)

class abonoForms( forms.ModelForm ):
	class Meta:
		model = abono
		exclude = ('cxp_id')
