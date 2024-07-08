from django import forms
from appointments.models import Appointment
class AppointmentForm(forms.ModelForm):  
    class Meta:  
        model = Appointment  
        fields = ['name', 'contact','age','preference']  