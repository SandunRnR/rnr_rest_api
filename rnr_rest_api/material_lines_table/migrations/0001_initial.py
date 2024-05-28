# Generated by Django 5.0.6 on 2024-05-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_version', models.FloatField()),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
