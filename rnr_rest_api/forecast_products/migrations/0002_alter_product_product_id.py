# Generated by Django 5.0.6 on 2024-05-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
