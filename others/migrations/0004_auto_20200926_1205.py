# Generated by Django 3.1.1 on 2020-09-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0003_job_apply_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='circular',
            name='slug',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='circular',
            name='job_title',
            field=models.CharField(max_length=255),
        ),
    ]
