# Generated by Django 4.0.4 on 2022-10-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_configuracion_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numero_CI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_contacto',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]