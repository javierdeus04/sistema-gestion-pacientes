# Generated by Django 4.0.4 on 2022-11-05 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('historiaclinica', '0011_alter_registro_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='firma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='registros', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
