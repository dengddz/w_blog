# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='article',
            name='icon',
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
