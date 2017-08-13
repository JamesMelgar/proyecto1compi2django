from django.shortcuts import render, redirect
from django.http import HttpResponse

#importamos el formulario
from apps.login.forms import LoginForm

def index(request):
	return render(request,'login/index.html')

def loguear_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			if nombre == 'admin':
				return render(request,'login/index.html')
			else:
				return  render(request, 'login/login_form.html', {'form':form})
	else:
		form = LoginForm()
	return  render(request, 'login/login_form.html', {'form':form})
# Create your views here.
