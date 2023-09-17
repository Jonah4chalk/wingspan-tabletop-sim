# Generated by Django 4.1.5 on 2023-09-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviary', '0004_foods_board_forest_nectar_board_grassland_nectar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdcard',
            name='direction_facing',
            field=models.CharField(choices=[('r', 'Right'), ('l', 'Left'), ('f', 'Forward')], default='f', max_length=1),
        ),
    ]
