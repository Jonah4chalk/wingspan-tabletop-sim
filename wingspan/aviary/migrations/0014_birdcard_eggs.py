# Generated by Django 4.1.5 on 2023-11-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviary', '0013_alter_board_forest_1_alter_board_forest_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdcard',
            name='eggs',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
