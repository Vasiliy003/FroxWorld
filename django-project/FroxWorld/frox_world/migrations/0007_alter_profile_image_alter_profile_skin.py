# Generated by Django 4.2.3 on 2023-08-31 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frox_world', '0006_profile_user_alter_profile_image_alter_profile_skin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skin',
            field=models.ImageField(blank=True, upload_to='skins/'),
        ),
    ]