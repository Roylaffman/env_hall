from django import forms
from models import *


class AddStandForm(forms.Form):
    """ Form that allows users to add a Stand model to the database."""
    coordinates = forms.CharField(max_length=200, required=True)
    name = forms.CharField(max_length=40, required=True)
    address = forms.CharField(max_length=200, required=True)
    descript = forms.CharField(max_length=200, required=True)

    def clean(self):
        cleaned_data = self.cleaned_data

        coordinates = cleaned_data.get("coordinates")
        name = cleaned_data.get("name")
        address = cleaned_data.get("address")
        descript = cleaned_data.get("descript")

        return cleaned_data


class AddProdForm(forms.ModelForm):
    """ Form that allows users to add a Produce model to the database."""
    class Meta:
        model = Produce
        fields = ['name', 'vegg', 'fruit', 'craft']
