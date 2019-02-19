from django import forms
from .models import *

class BuyersForm(forms.ModelForm):

    class Meta:
        model = Buyer
        exclude = [""]