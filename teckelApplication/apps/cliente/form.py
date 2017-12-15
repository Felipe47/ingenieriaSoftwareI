from django import forms
from apps.cliente.models import Cliente

class clienteFormulario(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'idCliente',
			'nombreCliente', 
			'apellidoCliente',
			'cedulaCliente',
			'barrioCliente',
			'direccionCliente',
			'correoCliente',
			'contraseñaCliente',
		]

		labels = {
			'idCliente': 'ID',
			'nombreCliente': 'Nombres', 
			'apellidoCliente': 'Apellidos',
			'cedulaCliente': 'Num Documento',
			'barrioCliente': 'Barrio',
			'direccionCliente': 'Direccion',
			'correoCliente': 'Ingrese el Correo',
			'contraseñaCliente': 'Ingrese la Contraseña',
		}

		widgets = {
			'idCliente': forms.TextInput(attrs={'class':'form-control'}),
			'nombreCliente': forms.TextInput(attrs={'class':'form-control'}), 
			'apellidoCliente': forms.TextInput(attrs={'class':'form-control'}),
			'cedulaCliente': forms.TextInput(attrs={'class':'form-control'}),
			'barrioCliente': forms.TextInput(attrs={'class':'form-control'}),
			'direccionCliente': forms.TextInput(attrs={'class':'form-control'}),
			'correoCliente': forms.TextInput(attrs={'class':'form-control'}),
			'contraseñaCliente': forms.TextInput(attrs={'class':'form-control'}),
		}
