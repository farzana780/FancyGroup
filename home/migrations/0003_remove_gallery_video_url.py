# Generated by Django 3.1.1 on 2020-10-05 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201005_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='video_url',
        ),
    ]
