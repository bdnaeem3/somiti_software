# Generated by Django 2.1.3 on 2018-11-17 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0001_initial'),
        ('reference', '0003_remove_reference_savings'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='savings',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='savings.Savings'),
        ),
    ]
