from django.shortcuts import render, redirect
#from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import membersForm
from .models import Members, Companyes
# Create your views here.
def become_member(request):

	'''member = Members.objects.filter(user=request.user)
			
				if member:
					return redirect('home')
			 '''
	if request.method == 'GET':
		form = membersForm()
		return render(request,'members_form.html',{'form':form})
	else:
	 	form = membersForm(request.POST)
	 	
	 	if form.is_valid():
	 		member = form.save(commit=False)
	 		member.user = request.user
	 		member.save()
	 		return redirect('home')
	 	else:
	 		return render(request,'members_form.html',{'form':form})


