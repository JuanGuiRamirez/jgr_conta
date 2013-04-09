from django import forms
from principal.models import *
from django.contrib.admin import widgets   
import datetime

class loginForms( forms.Form ):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class cxpForms( forms.ModelForm ):	
	class Meta:
		model = cxp
		exclude = ('monto_total',)

class abonoForms( forms.ModelForm ):
	fecha_abono = forms.DateField(initial=datetime.date.today)#widget=widgets.AdminDateWidget())
	#saldo_Inicial = forms.FloatField(initial=0)
	#saldo_final = forms.FloatField(initial=0)
	class Meta:
		model = abono		
		exclude = ('saldo_Inicial', 'cxp_id', 'saldo_final',)
