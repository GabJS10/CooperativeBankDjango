from django.db import models

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='home_auth/img', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	url = models.URLField(blank=True)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title	