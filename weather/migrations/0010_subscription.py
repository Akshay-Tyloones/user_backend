# Generated by Django 5.0.4 on 2024-05-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0009_delete_favouritecity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('connection_id', models.CharField(max_length=100)),
            ],
        ),
    ]
