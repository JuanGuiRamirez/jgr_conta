from django.db import models

class cxp( models.Model ):
	tercero = models.CharField(max_length=120)
	concepto = models.CharField(max_length=200)
	total_valor = models.FloatField()
	total_abono = models.FloatField()
	monto_total = models.FloatField()
	monto_neto = models.FloatField()


class abono( models.Model ):
	monto_abono = models.FloatField()
	fecha_abono = models.DateField(blank=True, null=True)
	saldo_Inicial = models.FloatField()
	saldo_final = models.FloatField()
	cxp_id = models.ForeignKey(cxp)
	


