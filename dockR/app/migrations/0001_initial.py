# Generated by Django 3.0 on 2019-12-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('data', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
