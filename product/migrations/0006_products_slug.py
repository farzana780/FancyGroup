# Generated by Django 3.1.1 on 2020-10-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201005_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
