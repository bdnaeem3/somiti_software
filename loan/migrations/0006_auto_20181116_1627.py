# Generated by Django 2.1.3 on 2018-11-16 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20181116_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reference.Reference'),
        ),
    ]
