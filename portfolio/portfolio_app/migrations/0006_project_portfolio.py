# Generated by Django 4.2 on 2024-03-01 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_alter_student_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
            preserve_default=False,
        ),
    ]
