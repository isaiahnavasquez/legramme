# Generated by Django 2.0.4 on 2018-04-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20180422_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_photo',
            field=models.ImageField(default='images/default/cover_default.jpg', upload_to='images/blog_covers'),
        ),
    ]
