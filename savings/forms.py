from django import forms
from . models import Savings


class DateInput(forms.DateInput):
    input_type = 'date'


class SavingsForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = '__all__'
        widgets = {
            'join_date': DateInput()
        }
