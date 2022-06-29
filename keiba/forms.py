from django import forms
from .models import Horse

class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ('name', 'age', 'sex',)
