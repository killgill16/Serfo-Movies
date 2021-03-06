# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-15 09:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_movie', models.ManyToManyField(to='info.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('review_title', models.CharField(max_length=30)),
                ('rating', models.FloatField(default=0, max_length=10)),
                ('content', models.TextField()),
                ('movie_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Movie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('device_id', models.CharField(max_length=50, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='core_users', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image_url', models.ImageField(blank=True, max_length=200, null=True, upload_to=b'user-images')),
                ('gender', models.CharField(blank=True, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'X', b'Other')], max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.UserProfile'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.UserProfile'),
        ),
    ]
