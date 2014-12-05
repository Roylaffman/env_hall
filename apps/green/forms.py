from django import forms
from models import *


class AddStandForm(forms.Form):

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

    class Meta:
        model = Produce
        fields = ['name', 'vegg', 'fruit', 'craft']


    # name = forms.ChoiceField()
    # vegg = forms.BooleanField()
    # fruit = forms.BooleanField()
    # craft = forms.BooleanField()
    #
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #
    #     name = cleaned_data.get("name")
    #     vegg = cleaned_data.get("vegg")
    #     fruit = cleaned_data.get("fruit")
    #     craft = cleaned_data.get("craft")
    #
    #     return cleaned_data