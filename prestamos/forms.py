from .models import Modality, Loans
from socios.models import Co_signer, Members
from django import forms
from django.core.validators import RegexValidator


class loansForm(forms.ModelForm):
	Modality = forms.ModelChoiceField(
		queryset=Modality.objects.all(),
		widget=forms.Select(attrs={'class':'form-control'})
		)

	def __init__(self, current_user, *args, **kwargs):
		super(loansForm, self).__init__(*args, **kwargs)
		self.fields['co_signer'].queryset= Co_signer.objects.filter(members__user=current_user)
		co_signer = forms.ModelChoiceField(
		queryset=self.fields['co_signer'].queryset,
		widget=forms.Select(attrs={'class':'form-control'})
		)
		
		
 
	class Meta:
		model = Loans
		fields = ['Modality','value','term_months','co_signer']
		widgets = {
			'value': forms.NumberInput(attrs={'class':'form-control','placeholder':'$'}),
			#'monthly_fee': forms.NumberInput(attrs={'class':'form-control','placeholder':'$'}),
			'term_months': forms.NumberInput(attrs={'class':'form-control','placeholder':'Maximun time'}),
		}

class cosigners_form(forms.ModelForm):
	phone = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'type cosigner phone'}),
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
		model = Co_signer
		fields = ['name','dni','from_city','phone','address','email','potential_client']
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name of cosigner'}),
			'from_city': forms.TextInput(attrs={'class':'form-control','placeholder':'Where cosigner from'}),
			'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Write the address of your cosigner'}),
			'email': forms.TextInput(attrs={'class':'form-control','placeholder':'The emails cosigner'}),
			'potential_client': forms.CheckboxInput(attrs={'class':'form-check-input'}),
		}