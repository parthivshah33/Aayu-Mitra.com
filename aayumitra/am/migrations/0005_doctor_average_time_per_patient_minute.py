# Generated by Django 3.1.7 on 2021-05-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0004_auto_20210511_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='average_time_per_patient_minute',
            field=models.CharField(default='30 minute', max_length=4),
        ),
    ]
