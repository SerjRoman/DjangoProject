from django import forms
from .models import Rewiews

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Rewiews
        fields = ("name","email", "text")