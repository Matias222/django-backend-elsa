# Generated by Django 5.1 on 2024-08-20 21:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_adopcion_adoptante_alter_adopcion_animal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
