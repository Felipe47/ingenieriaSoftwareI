from django.db import models

# Create your models here.


class Pedido(models.Model):
	tipoPedido = models.CharField(max_length=50)
	domicilioPedido = models.CharField(max_length=50)
	fechaPedido = models.DateField()
	valorPedido = models.IntegerField()

	

class Producto(models.Model):
	idProducto = models.CharField(max_length=50, primary_key=True)
	nombreProducto = models.CharField(max_length=50)
	precioProducto = models.IntegerField(null=True)
	descripcionProducto = models.CharField(max_length=100, null=True)
	pedido = models.ManyToManyField(Pedido)

	def __str__(self):
		return '{}'.format(self.idProducto)