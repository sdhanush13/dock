# Generated by Django 3.0 on 2019-12-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191203_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='time',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
