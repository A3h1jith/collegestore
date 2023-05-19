from django import forms
from .models import Message
class messageForm(forms.ModelForm):
    class Meta:
        model=Messages
        fields=['name','email','subject','Message']