# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20160722_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_thumbnail',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
