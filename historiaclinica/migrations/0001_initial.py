# Generated by Django 4.0.4 on 2022-11-05 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('panel', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('resumen', models.CharField(max_length=30)),
                ('contenido', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='paraclinica')),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='registros', to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='panel.paciente')),
            ],
        ),
    ]
