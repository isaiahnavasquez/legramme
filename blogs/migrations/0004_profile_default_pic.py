# Generated by Django 2.0.4 on 2018-04-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_pic',
            field=models.ImageField(default='images/default/empty-profile.png', upload_to='images/profiles/'),
        ),
    ]