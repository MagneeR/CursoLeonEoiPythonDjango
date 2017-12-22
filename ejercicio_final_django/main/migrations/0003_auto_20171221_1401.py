# Generated by Django 2.0 on 2017-12-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171221_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='combat',
            options={'verbose_name': 'Combate', 'verbose_name_plural': 'Combates'},
        ),
        migrations.AddField(
            model_name='fighter',
            name='force',
            field=models.IntegerField(default=4, verbose_name='Fuerza'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='resistance',
            field=models.IntegerField(default=3, verbose_name='Resistencia'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='skill',
            field=models.IntegerField(default=3, verbose_name='Habilidad'),
        ),
    ]
