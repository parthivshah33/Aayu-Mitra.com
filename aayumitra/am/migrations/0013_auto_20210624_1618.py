# Generated by Django 3.1.7 on 2021-06-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0012_auto_20210623_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='confirmation_code',
            field=models.CharField(default='0000', max_length=10),
        ),
    ]
