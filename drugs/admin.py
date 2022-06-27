from django.contrib import admin
from .models import DemoDrug, Quantity, Day, Time
# Register your models here.
admin.site.register(DemoDrug)
admin.site.register(Quantity)
admin.site.register(Day)
admin.site.register(Time)