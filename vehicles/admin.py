from django.contrib import admin

# Register your models here.
from .models import ODVehicle
from .forms import ODVehicleForm

class VehicleAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "driver", "number", "capacity"]
    form = ODVehicleForm

admin.site.register(ODVehicle,VehicleAdmin)