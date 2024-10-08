# Generated by Django 5.1 on 2024-08-17 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_comuna_region'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comunas', to='main.region'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmueble', to='main.comuna'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmueble', to=settings.AUTH_USER_MODEL),
        ),
    ]
