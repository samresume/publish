# Generated by Django 4.1.5 on 2023-01-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarflare', '0003_alter_project_datetime_alter_project_report_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='access',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
    ]