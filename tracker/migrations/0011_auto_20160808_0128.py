# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20160808_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='time_requested',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='time_resolved',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
