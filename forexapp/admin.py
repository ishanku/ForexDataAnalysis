from django.contrib import admin
from .models import ForexCurrent
from .models import ForexHistoric
# Register your models here.

class ForexCurrentAdmin(admin.ModelAdmin):
    list_display = ('Date', 'AUD','EUR','NZD','GBP','BRL','CAD','CNY','HKD','INR','KRW','MXN','ZAR')

admin.site.register(ForexCurrent, ForexCurrentAdmin)

class ForexHistoricAdmin(admin.ModelAdmin):
    list_display = ('Date', 'AUD','EUR','NZD','GBP','BRL','CAD','CNY','HKD','INR','KRW','MXN','ZAR')

admin.site.register(ForexHistoric, ForexHistoricAdmin)
