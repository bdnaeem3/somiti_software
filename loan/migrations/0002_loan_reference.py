# Generated by Django 2.1.3 on 2018-11-16 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='reference',
            field=models.ForeignKey(choices=[('Tajibul Mir', 'Tajibul Mir')], null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reference.Reference'),
        ),
    ]