from django import forms
from .models import SMS

class SMSForm(forms.ModelForm):
    class Meta:
        model = SMS
        fields = ['to_number', 'message']
        widgets = {
            'to_number': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
