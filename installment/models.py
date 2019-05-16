from django.db import models
from loan.models import Loan
from savings.models import Savings
from reference.models import Reference


class LoanInstallment(models.Model):

    status = (
        ('1', 'Unpaid'),
        ('2', 'Paid'),
    )

    installment = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    name = models.ForeignKey(Loan, null=True, on_delete=models.DO_NOTHING)
    pay_to = models.ForeignKey(Reference, null=True, on_delete=models.DO_NOTHING)
    pay_date = models.DateField(null=False)
    installment = models.CharField(max_length=2, choices=installment)

    def __str__(self):
        return self.name.name + ' has paid his loan to ' + self.pay_to.name


class SavingsInstallment(models.Model):

    status = (
        ('1', 'Unpaid'),
        ('2', 'Paid'),
    )

    installment = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    name = models.ForeignKey(Savings, null=True, on_delete=models.DO_NOTHING)
    pay_to = models.ForeignKey(Reference, null=True, on_delete=models.DO_NOTHING)
    pay_date = models.DateField(null=False)
    installment = models.CharField(max_length=2, choices=installment)

    def __str__(self):
        return self.savings.name + ' has paid his loan to ' + self.reference.name
