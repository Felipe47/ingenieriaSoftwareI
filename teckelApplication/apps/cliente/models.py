from django.db import models

# Create your models here.

#class Pedido(models.Model):
	#tipoPedido = models.CharField(max_length=50)
	#domicilioPedido = models.CharField(max_length=50)

class Cliente(models.Model):
	idCliente = models.CharField(max_length=50, primary_key=True)
	nombreCliente = models.CharField(max_length=50)
	apellidoCliente = models.CharField(max_length=50)
	cedulaCliente = models.IntegerField()
	barrioCliente = models.CharField(max_length=50)
	direccionCliente = models.CharField(max_length=50)
	correoCliente = models.EmailField()
	contraseñaCliente = models.CharField(max_length=50)
	#pedido = models.ManyToManyField(Pedido)

	def __str__(self):
		return '{}'.format(self.nombreCliente)
