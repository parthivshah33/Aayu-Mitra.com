# Generated by Django 3.1.7 on 2022-04-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0026_auto_20220310_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='clinic_active_status',
            field=models.BooleanField(default=True),
        ),
    ]
