# Generated by Django 4.0.4 on 2022-11-07 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_disponibilidad_horaria_solicitudpaciente_disponibilidad_horaria_final_and_more'),
        ('panel', '0002_alter_paciente_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.solicitudpaciente'),
        ),
    ]
