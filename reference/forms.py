from django import forms
from . models import Reference


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'address', 'mobile', 'nid']
