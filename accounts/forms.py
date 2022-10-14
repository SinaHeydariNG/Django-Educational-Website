from dataclasses import field
from django import forms
from .models import Messages , CustomUser
from django.core.exceptions import ValidationError
class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['title','subject','text']

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise ValidationError("At least 10 charachter required :)")
        return text    

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','image','first_name','last_name','address','phone_number']
