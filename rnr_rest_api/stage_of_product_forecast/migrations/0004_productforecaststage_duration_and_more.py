# Generated by Django 5.0.4 on 2024-07-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_of_product_forecast', '0003_alter_productforecaststage_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productforecaststage',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productforecaststage',
            name='next_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productforecaststage',
            name='next_stage',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='productforecaststage',
            name='previous_stage',
            field=models.CharField(default='null', max_length=255),
        ),
    ]