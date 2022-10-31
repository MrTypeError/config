from django import forms
from .models import Shortner


class ShortnerFrom(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"placeholder": "LONG URL"}))

    class Meta:
        model = Shortner
        fields = ("long_url",)
