# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_maintenance_is_seen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintainer',
            old_name='user_contact',
            new_name='contact',
        ),
    ]
