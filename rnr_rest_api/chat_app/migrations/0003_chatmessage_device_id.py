# Generated by Django 5.0.6 on 2024-07-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_chatmessage_created_at_chatmessage_next_action_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='device_id',
            field=models.CharField(default='null', max_length=255),
        ),
    ]