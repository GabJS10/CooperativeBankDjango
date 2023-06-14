from django.contrib import admin
from .models import Articles
# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)

admin.site.register(Articles,ArticlesAdmin)	