# Generated by Django 5.0.1 on 2024-02-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_emimodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='emimodels',
            name='emi',
            field=models.IntegerField(default='1000'),
        ),
    ]
