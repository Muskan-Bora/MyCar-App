# Generated by Django 5.0.1 on 2024-03-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_satisfied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Satisfied', models.CharField(default='satisfied', max_length=200)),
            ],
        ),
    ]