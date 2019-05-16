from django import forms
from . models import LoanInstallment, SavingsInstallment


class DateInput(forms.DateInput):
    input_type = 'date'


class LoanInstallmentForm(forms.ModelForm):
    class Meta:
        model = LoanInstallment
        fields = ['name', 'pay_to', 'pay_date', 'installment']
        widgets = {
            'pay_date': DateInput()
        }


class SavingsInstallmentForm(forms.ModelForm):
    class Meta:
        model = SavingsInstallment
        fields = ['name', 'pay_to', 'pay_date', 'installment']
        widgets = {
            'pay_date': DateInput()
        }
