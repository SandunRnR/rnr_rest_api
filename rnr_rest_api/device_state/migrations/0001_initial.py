# Generated by Django 5.0.6 on 2024-05-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('command', models.CharField(max_length=100)),
            ],
        ),
    ]