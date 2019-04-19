from django.contrib import admin
from .models import Portfolio
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','image','description','ext_link','start_date','end_date','is_active')
    prepopulated_fields = {'slug': ('title',)}        

admin.site.register(Portfolio, PortfolioAdmin)
