# Generated by Django 3.2.13 on 2022-11-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_location_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='desc',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]