# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160808_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]
