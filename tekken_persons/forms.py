from django import forms
from . import models


class TekkenForm(forms.ModelForm):
    class Meta:
        model = models.PersonGame
        fields = '__all__'


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'
