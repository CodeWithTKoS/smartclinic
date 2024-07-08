from django import forms
from doctor.models import Doctor
class DoctorForm(forms.ModelForm):  
    class Meta:  
        model = Doctor  
        fields = ['name', 'contact', 'pwd']
        widgets = {
            'contact': forms.TextInput(attrs={'autocomplete': 'off'}),
            'pwd' : forms.PasswordInput(attrs={'autocomplete': 'new-password','data-toggle' : 'password',}),
        }

