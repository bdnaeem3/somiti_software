# Generated by Django 2.1.3 on 2018-12-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_remove_loan_installment'),
        ('installment', '0008_savingsinstallment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaninstallment',
            name='name',
        ),
        migrations.AddField(
            model_name='loaninstallment',
            name='name',
            field=models.ManyToManyField(null=True, to='loan.Loan'),
        ),
    ]
