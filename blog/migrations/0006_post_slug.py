# Generated by Django 3.1.1 on 2020-10-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200930_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='details', max_length=255),
        ),
    ]