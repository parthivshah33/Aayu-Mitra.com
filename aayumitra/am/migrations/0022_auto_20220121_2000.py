# Generated by Django 3.1.7 on 2022-01-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0021_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
