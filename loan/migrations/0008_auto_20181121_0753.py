# Generated by Django 2.1.3 on 2018-11-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0007_auto_20181117_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='installment_no',
            field=models.CharField(default=0, max_length=2, null=True),
        ),
    ]
