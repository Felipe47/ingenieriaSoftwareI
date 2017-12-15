from django.conf.urls import url, include

from apps.cliente.views import index, cliente_view

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^nuevo$', cliente_view, name='cliente_crear'),
	
	]