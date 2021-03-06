# Generated by Django 2.0 on 2017-12-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171221_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='force',
            field=models.PositiveIntegerField(default=4, verbose_name='Fuerza'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='resistance',
            field=models.PositiveIntegerField(default=3, verbose_name='Resistencia'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='skill',
            field=models.PositiveIntegerField(default=3, verbose_name='Habilidad'),
        ),
    ]
