from django import forms
from . models import Loan


class DateInput(forms.DateInput):
    input_type = 'date'


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan

        fields = ['name', 'address', 'mobile', 'nid', 'amount', 'join_date', 'reference']
        widgets = {
            'join_date': DateInput()
        }
