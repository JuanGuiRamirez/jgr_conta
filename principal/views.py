from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from principal.formularios import *
from principal.models import *

#==============================================================#

def index(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/inicio')
	else:	
		if request.method == "POST":
			formulario = loginForms( request.POST )
			if formulario.is_valid():
				usuario = formulario.cleaned_data["username"]
				contra = formulario.cleaned_data["password"]
				acceso = authenticate(username=usuario, password=contra)
				if acceso is not None and acceso.is_active:
					login( request, acceso )
					return HttpResponseRedirect('/inicio')
				else:
					mensaje = 'Los datos son incorrectos'

		formulario = loginForms()
		return render_to_response('index.html', {"formulario":formulario, "mensaje":mensaje}, context_instance=RequestContext(request))

#==============================================================#

@login_required(login_url='/')
def inicio(request):
	cuentas = cxp.objects.all()
	return render_to_response('inicio.html', {'cuentas':cuentas}, context_instance=RequestContext(request))

#==============================================================#

@login_required(login_url='/')
def agregar_cuenta(request):
	if request.method == "POST":
		formulario_cuenta = cxpForms( request.POST )
		if formulario_cuenta.is_valid():
			ins_save = formulario_cuenta.save( commit = False)
			ins_save.monto_total = (ins_save.total_valor - ins_save.total_abono)
			formulario_cuenta.save()
			return HttpResponseRedirect('/inicio')		
	else:
		formulario_cuenta = cxpForms()

	return render_to_response('agregar_cuenta.html', {'formulario':formulario_cuenta}, context_instance=RequestContext(request))

#==============================================================#

def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')

#==============================================================#

@login_required(login_url='/')
def editar_cuenta(request, cuenta_id):
	cuenta = cxp.objects.get( pk=cuenta_id )
	if request.method == "POST":
		formulario_cuenta = cxpForms(request.POST, instance=cuenta)
		if formulario_cuenta.is_valid():
			formulario_cuenta.save()
			return HttpResponseRedirect("/")
	else:
		formulario_cuenta = cxpForms(instance=cuenta)
	return render_to_response('editar_cuenta.html', {'formulario':formulario_cuenta}, context_instance=RequestContext(request))

#==============================================================#

@login_required(login_url=('/'))
def agregar_abono(request, cxp_id):	
	cuenta_pagar = cxp.objects.get(pk=cxp_id)
	abonos = abono.objects.filter(cxp_id=cxp_id)
	if request.method == "POST":
		mensaje = 'true'
		formulario = abonoForms( request.POST )
		if formulario.is_valid:			
			ins_save = formulario.save( commit = False )
			ins_save.cxp_id_id = cxp_id
			ins_save.saldo_Inicial = cuenta_pagar.monto_total
			ins_save.saldo_final = (ins_save.saldo_Inicial - ins_save.monto_abono)
			ins_save.save()			
			return HttpResponseRedirect("/inicio")
	else:		
		formulario = abonoForms()		
	return render_to_response('agregar_abono.html', {"formulario":formulario, "abonos":abonos, "cuenta":cuenta_pagar}, context_instance=RequestContext(request))