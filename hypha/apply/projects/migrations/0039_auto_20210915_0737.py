# Generated by Django 2.2.24 on 2021-09-15 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0038_add_deliverable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverable',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverables', to='application_projects.Project'),
        ),
    ]
