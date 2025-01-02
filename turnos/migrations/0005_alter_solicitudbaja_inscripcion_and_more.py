# Generated by Django 5.1.4 on 2024-12-16 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0004_alter_turno_max_inscripciones'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudbaja',
            name='inscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_baja', to='turnos.inscripcion'),
        ),
        migrations.AddConstraint(
            model_name='inscripcion',
            constraint=models.UniqueConstraint(fields=('turno', 'usuario'), name='unique_user_turno'),
        ),
        migrations.AddConstraint(
            model_name='solicitudbaja',
            constraint=models.UniqueConstraint(fields=('inscripcion',), name='unique_solicitud_baja_per_inscripcion'),
        ),
    ]