# Generated by Django 2.1.3 on 2018-11-16 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20181116_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='reference',
            field=models.ForeignKey(choices=[(1, 'Tajibul Mir'), (2, 'Sohel Rana')], null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reference.Reference'),
        ),
    ]
