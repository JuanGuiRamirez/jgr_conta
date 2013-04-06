from django import forms
from principal.models import *

class loginForms( forms.Form ):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class cxpForms( forms.ModelForm ):	
	class Meta:
		model = cxp
		exclude = ('monto_total',)
