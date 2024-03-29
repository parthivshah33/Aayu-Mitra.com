# Generated by Django 3.1.7 on 2021-05-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('am', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('user_phone_number', models.CharField(max_length=15)),
                ('user_email_id', models.CharField(max_length=25)),
                ('user_suggesstion', models.CharField(max_length=3000, null=True)),
                ('user_query', models.CharField(max_length=3000, null=True)),
                ('user_Complain', models.CharField(max_length=3000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email_id',
            field=models.EmailField(max_length=30),
        ),
    ]
