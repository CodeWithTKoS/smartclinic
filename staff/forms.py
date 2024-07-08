from django import forms
from staff.models import Staff
class StaffForm(forms.ModelForm):  
    class Meta:  
        model = Staff  
        fields = ['name', 'contact', 'pwd']
        widgets = {
            'contact': forms.TextInput(attrs={'autocomplete': 'off'}),
            'pwd' : forms.PasswordInput(attrs={'autocomplete': 'new-password','data-toggle' : 'password',}),
        }  

