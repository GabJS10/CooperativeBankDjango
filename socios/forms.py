from .models import Members
from django import forms
from django.core.validators import RegexValidator


class membersForm(forms.ModelForm):
	phone = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'type your phone'}),
		validators=[
			RegexValidator(r'^[0-9]{10}$', 'Ingrese solo números del 1 al 9 y asegúrese de tener exactamente 10 dígitos.')
		]

		)

	dni = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'a valid DNI'}),
		validators=[
			RegexValidator(r'^[0-9]{10}$', 'Ingrese un dni valido.')
		]

		)

	class Meta:
		model = Members
		fields = ['name','dni','phone','address','email','monthly_salary','company_id']
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control','placeholder':'your name '}),
			'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Write your address'}),
			'email': forms.TextInput(attrs={'class':'form-control','placeholder':'type your email'}),
			'monthly_salary': forms.NumberInput(attrs={'class':'form-control','placeholder':'$'}),
		}