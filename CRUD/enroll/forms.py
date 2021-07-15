from django import forms
from django.core import validators
from .models import studentinfo

class studentforms(forms.ModelForm):
    class Meta:
        model=studentinfo
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'} ),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            
            }

