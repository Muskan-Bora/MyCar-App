# Generated by Django 5.0.1 on 2024-03-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_location_city_location_state_alter_location_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='name', max_length=200),
        ),
    ]