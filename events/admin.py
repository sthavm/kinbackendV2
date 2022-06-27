from django.contrib import admin
from .models import Event, DispensedDrug, DispensedSession
# Register your models here.
admin.site.register(Event)
admin.site.register(DispensedDrug)
admin.site.register(DispensedSession)
