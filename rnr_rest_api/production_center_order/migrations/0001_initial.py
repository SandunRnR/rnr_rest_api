# Generated by Django 5.0.6 on 2024-07-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_number', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('production_type', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
