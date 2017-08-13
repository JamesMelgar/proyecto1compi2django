from django import forms

from apps.login.models import mlogin

class LoginForm(forms.ModelForm):

	class Meta:
		model = mlogin

		fields = [
			'nombre',
			'contraseña',
		]
		labels = {
			'nombre': 'Nombre',
			'contraseña': 'Contraseña',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'contraseña':forms.TextInput(attrs={'class':'form-control'}),
		}