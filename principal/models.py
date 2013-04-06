from django.db import models

class cxp( models.Model ):
	tercero = models.CharField(max_length=120)
	concepto = models.CharField(max_length=200)
	total_valor = models.FloatField()
	total_abono = models.FloatField()
	monto_total = models.FloatField() #default='0')#, required=false)

