# Generated by Django 4.2 on 2024-03-01 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_student_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='portfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
    ]