# Generated by Django 4.2 on 2024-04-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goteach_app', '0005_alter_class_presentation_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='ended',
            field=models.BooleanField(default=False),
        ),
    ]