from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cliente.form import clienteFormulario
# Create your views here.

def index(request):
	return render(request, 'cliente/index.html')

def cliente_view(request):
	if request.method == 'POST':
		form = clienteFormulario(request.POST)
		if form.is_valid():
				form.save()
		return redirect('cliente:index')
	else:
		form = clienteFormulario()

	return render(request, 'Cliente/cliente_form.html', {'form':form})