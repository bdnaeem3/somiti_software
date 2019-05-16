# Generated by Django 2.1.3 on 2018-11-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_remove_reference_savings'),
        ('loan', '0010_remove_loan_installment'),
        ('installment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='loan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='loan.Loan'),
        ),
        migrations.AddField(
            model_name='installment',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reference.Reference'),
        ),
    ]
