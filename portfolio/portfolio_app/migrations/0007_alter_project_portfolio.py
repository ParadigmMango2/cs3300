# Generated by Django 4.2 on 2024-03-14 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_project_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio_app.portfolio'),
        ),
    ]