# Generated by Django 3.1.1 on 2020-09-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_apply',
            name='department_name',
        ),
        migrations.AlterField(
            model_name='department_name',
            name='department_name',
            field=models.CharField(max_length=50),
        ),
    ]
