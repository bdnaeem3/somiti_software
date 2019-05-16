# Generated by Django 2.1.3 on 2018-11-24 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_remove_reference_savings'),
        ('savings', '0001_initial'),
        ('installment', '0007_auto_20181124_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsInstallment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField()),
                ('installment', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='savings.Savings')),
                ('pay_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reference.Reference')),
            ],
        ),
    ]
