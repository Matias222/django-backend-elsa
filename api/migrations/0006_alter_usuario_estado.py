# Generated by Django 5.1 on 2024-08-21 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('administrador', 'Administrador')], default='Activo', max_length=20),
        ),
    ]
