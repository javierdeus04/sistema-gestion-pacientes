# Generated by Django 4.0.4 on 2022-10-30 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_configuracion_nombre_clinica_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='numero_ci',
            new_name='numero_CI',
        ),
    ]