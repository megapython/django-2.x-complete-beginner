# Generated by Django 2.2.4 on 2019-08-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avataar',
            field=models.ImageField(default='default_user.png', upload_to='profile_pics/'),
        ),
    ]
