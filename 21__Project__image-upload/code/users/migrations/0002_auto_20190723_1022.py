# Generated by Django 2.2.3 on 2019-07-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Email already exists, try registering with different email.'}, max_length=255, unique=True),
        ),
    ]
