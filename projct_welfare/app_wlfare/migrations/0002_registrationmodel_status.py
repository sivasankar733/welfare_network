# Generated by Django 3.0.4 on 2020-04-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_wlfare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='status',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
