# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='feat_photos',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
