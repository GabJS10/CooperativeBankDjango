from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import registerForm
from .models import Articles
from socios.views import Members
# Create your views here.
def home(request):
	articles = Articles.objects.all()
	if request.user.is_authenticated:
		member = Members.objects.filter(user=request.user)
		if member:
			print('entro en el if')
			request.session['is_member'] = True

	print(request.session.get('is_member'))		
	return render(request,'home.html',{'articles':articles})

def log_out(request):
	logout(request)
	return redirect('home')

def signin(request):
	if request.method == 'GET':
		form = AuthenticationForm()
		return render(request,'signin.html',{'form':form})
	else:
		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			user = authenticate(username=username,password=password)


			if user is None:
				mensajes.error(request,'El usuario no existe')
			else:
				login(request,user)
				return redirect('home')	

		else:
			for error in form.error_messages:
				messages.error(request,form.error_messages[error])

			return render(request,'signin.html',{'form':form}) 	



def register(request):
	
	if request.method == 'GET':
		form = registerForm()
		return render(request,'register_form.html',{'form':form})
	else:
		form = registerForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('home')
		else:
			for error in form.error_messages:
				messages.error(request,form.error_messages[error])

			return render(request,'register_form.html',{'form':form}) 	

		