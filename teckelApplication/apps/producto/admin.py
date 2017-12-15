from django.contrib import admin
from apps.producto.models import Producto
from apps.producto.models import Pedido
# Register your models here.

admin.site.register(Producto)
admin.site.register(Pedido)