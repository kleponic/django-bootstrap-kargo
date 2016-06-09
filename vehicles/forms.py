from django import forms
from django.utils.translation import ugettext_lazy as _
from vehicles.models import ODVehicle


class ODVehicleForm(forms.ModelForm):
    """
    Form to manage vehicle data-entry
    """
   

    class Meta:
        model = ODVehicle
        fields = ('name', 'driver', 'number', 'capacity', 'photo')