# Generated by Django 3.1.7 on 2021-07-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0018_auto_20210703_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='dateTime',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]