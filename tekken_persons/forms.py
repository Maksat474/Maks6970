from django import forms
from . import models


class TekkenForm(forms.ModelForm):
    class Meta:
        model = models.PersonGame
        fields = '__all__'
