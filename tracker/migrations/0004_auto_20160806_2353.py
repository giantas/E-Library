# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0003_auto_20160806_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=100)),
                ('time_raised', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=7)),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='in-progress', max_length=12)),
                ('time_resolved', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments', models.CharField(blank=True, default='', max_length=255)),
                ('is_seen', models.BooleanField(default=False)),
                ('handler', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='issue_handler', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='issuehandle',
            name='handler',
        ),
        migrations.RemoveField(
            model_name='issuehandle',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='user',
        ),
        migrations.DeleteModel(
            name='IssueHandle',
        ),
        migrations.DeleteModel(
            name='Issues',
        ),
    ]
