# Generated by Django 3.0 on 2019-12-09 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_addpost_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
