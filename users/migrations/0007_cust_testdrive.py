# Generated by Django 5.0.1 on 2024-02-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_TestDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salutation', models.CharField(default='Mr/Mrs./Ms.', max_length=50)),
                ('FirstName', models.CharField(default='First Name', max_length=100)),
                ('LastName', models.CharField(default='Last Name', max_length=200)),
                ('EmailID', models.CharField(default='Email Id', max_length=100)),
                ('MobileNo', models.CharField(default='Mobile Number', max_length=100)),
                ('PreferredCity', models.CharField(default='Preferred City', max_length=500)),
            ],
        ),
    ]
