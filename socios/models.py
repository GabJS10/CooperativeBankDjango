from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Companyes(models.Model):
	name = models.CharField(max_length=100)
	dni_company = models.CharField(max_length=10, unique=True)
	contact_person = models.CharField(max_length=100)
	number_of_employees = models.IntegerField()

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Companyes'

	def __str__(self):
		return self.name	

class Co_signer(models.Model):
	name = models.CharField(max_length=100)
	dni = models.CharField(max_length=10, unique=True)
	from_city = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	address	= models.CharField(max_length=50)
	email = models.EmailField()
	potential_client = models.BooleanField()

	class Meta:
		verbose_name = 'co_signer'
		verbose_name_plural = 'co_signers'

	def __str__(self):
		return self.name	

class Members(models.Model):
	name = models.CharField(max_length=100)
	dni = models.CharField(max_length=10, unique=True)
	phone = models.CharField(max_length=10)
	address	= models.CharField(max_length=50)
	email = models.EmailField()
	monthly_salary = models.DecimalField(max_digits=10,decimal_places=2)
	company_id = models.ForeignKey(Companyes, on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
	co_signers = models.ManyToManyField(Co_signer)

	class Meta:
		verbose_name = 'Member'
		verbose_name_plural = 'Members'

	def __str__(self):
		return self.name	
