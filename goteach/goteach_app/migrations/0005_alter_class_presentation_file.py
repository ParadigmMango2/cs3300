# Generated by Django 4.2 on 2024-04-17 17:23

from django.db import migrations, models
import goteach_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('goteach_app', '0004_class_presentation_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='presentation_file',
            field=models.FileField(blank=True, null=True, upload_to='presentations', validators=[goteach_app.validators.validate_presentation_file]),
        ),
    ]
