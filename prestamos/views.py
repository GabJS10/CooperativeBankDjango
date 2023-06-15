from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Modality, Loans
from socios.models import Co_signer, Members
from .forms import loansForm, cosigners_form
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def make_loan(request):

	cosigners = Co_signer.objects.filter(members__user=request.user)

	if cosigners:
		if request.method == 'GET':
			form = loansForm(current_user=request.user)

			return render(request,'make_loan.html',{'form':form})
		else:
			form = loansForm(request.user,request.POST)

			if form.is_valid():
				loan = form.save(commit=False)
				m = Members.objects.get(user=request.user)
				loan.Members = m
				mf= int(loan.value/loan.term_months)
				loan.monthly_fee = mf
				loan.save()
				return redirect('home')
			else:
				return render(request,'make_loan.html',{'form':form})
	else:
		form = cosigners_form()
		print('entro a else')
		mensaje= 'Necesitas haber registrado al menos un codeudor para hacer el prestamo'
		return render(request,'co_signer.html',{'form':form,'mensaje':mensaje})			

@login_required
def create_cosigner(request):

	if request.method== 'POST':
		form_cosigner = cosigners_form(request.POST)

		if form_cosigner.is_valid():
			cosigner = form_cosigner.save(commit=False)

			member = Members.objects.filter(dni=cosigner.dni)

			if member:
				mensaje = 'No se pudo registrar el codeudor, recuerda que esta persona no debe ser un socio de la cooperativa'
				return render(request,'co_signer.html',{'form':form_cosigner,'mensaje':mensaje})

			cosigner.save()

			m = Members.objects.get(user=request.user)

			m.co_signers.add(cosigner)	

			return redirect('home')

		return render(request,'co_signer.html',{'form':form_cosigner})			
	form_cosigner = cosigners_form()
	return render(request,'co_signer.html',{'form':form_cosigner})

@login_required
def all_loans(request):

	m = Members.objects.get(user=request.user)

	loans = Loans.objects.filter(Members=m).order_by('-start_date')

	return render(request,'view_loans.html',{'loans':loans})

@login_required
def replace_cosigner(request,cosigner_id):
	if request.method == 'GET':
		form = cosigners_form()
		c = Co_signer.objects.filter(members__user=request.user).exclude(pk=cosigner_id)
		return render(request,'replace_cosigner.html',{'form':form,'cosigners':c,'c_id':cosigner_id})

	form = cosigners_form(request.POST)
	m = Members.objects.get(user=request.user)

	try:
		if form.is_valid():
			

			cosigner = get_object_or_404(Co_signer,pk=cosigner_id)
			cosigner.delete()

			new_consigner = form.save(commit=False)

			new_consigner.save()

			m.co_signers.add(new_consigner)

			loans = Loans.objects.filter(Members=m)

			for loan in loans:
				if loan.co_signer==None:
					loan.co_signer=new_consigner
					loan.save()
			return redirect('view_loans')	
	except:
		return render(request,'replace_cosigner.html',{'form':form})

	return render(request,'replace_cosigner.html',{'form':form})

@login_required
def replace_for_old_cosigner(request,cosigner_id):
	if request.method=='POST':
		c_select = int(request.POST['cosigner_select'])

		
		cosigner = get_object_or_404(Co_signer,pk=c_select)
		m = Members.objects.get(user=request.user)
		loans = Loans.objects.filter(Members=m)
		c_delete = get_object_or_404(Co_signer,pk=cosigner_id)
			
		c_delete.delete()
		for loan in loans:
			if loan.co_signer==None:
				loan.co_signer=cosigner
				loan.save()
		return redirect('view_loans')	

@login_required
def all_cosigners(request):
	c = Co_signer.objects.filter(members__user=request.user)

	return render(request,'all_cosigners.html',{'cosigners':c})

@login_required
def loans_cosigner(request,cosigner_id):
	loans = Loans.objects.filter(co_signer__id=cosigner_id).order_by('-start_date')

	return render(request,'view_loans.html',{'loans':loans})