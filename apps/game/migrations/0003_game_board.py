# Generated by Django 2.0.6 on 2019-06-22 22:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190622_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], size=None),
        ),
    ]
