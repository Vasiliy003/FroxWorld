# Generated by Django 4.2.3 on 2023-07-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frox_world', '0004_delete_user_server_max_online_server_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='is_online',
            field=models.BooleanField(default=True),
        ),
    ]