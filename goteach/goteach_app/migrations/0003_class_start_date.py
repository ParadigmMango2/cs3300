# Generated by Django 4.2 on 2024-04-06 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goteach_app', '0002_rename_gamelink_class_game_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
