# Generated by Django 5.0.4 on 2024-05-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_alter_userdetails_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='cognito_user',
            field=models.CharField(default='hello', max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
