# Generated by Django 5.1.7 on 2025-03-28 03:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0009_alter_participante_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='nome',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
