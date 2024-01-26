from django import forms
from . import models


class TvshowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields =  '__all__'


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'


