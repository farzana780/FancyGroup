# Generated by Django 3.1.1 on 2020-10-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_summery',
            field=models.TextField(default='product'),
        ),
    ]
