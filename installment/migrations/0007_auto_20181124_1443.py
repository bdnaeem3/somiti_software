# Generated by Django 2.1.3 on 2018-11-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_remove_loan_installment'),
        ('reference', '0005_remove_reference_savings'),
        ('installment', '0006_auto_20181124_1413'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Installment',
            new_name='LoanInstallment',
        ),
    ]
