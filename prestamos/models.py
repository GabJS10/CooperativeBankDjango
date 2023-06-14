from django.db import models
from socios.models import Members, Co_signer
# Create your models here.
class Modality(models.Model):
	name = models.CharField(max_length=100, default=None)
	stipulated_time = models.IntegerField()
	interest_rate = models.DecimalField(max_digits=5,decimal_places=2)

	class Meta:
		verbose_name = 'Modality'
		verbose_name_plural = 'Modalitys'

	def __str__(self):
		return self.name	

class Loans(models.Model):
	Modality = models.ForeignKey(Modality, on_delete= models.CASCADE)
	Members = models.ForeignKey(Members, on_delete=models.CASCADE)
	start_date = models.DateTimeField(auto_now_add=True)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	monthly_fee = models.IntegerField()
	term_months = models.IntegerField()
	co_signer = models.ForeignKey(Co_signer,on_delete=models.SET_NULL, null=True)

	class Meta:
		verbose_name = 'Loan'
		verbose_name_plural = 'Loans'

	def __str__(self):
		return str(self.start_date)	
