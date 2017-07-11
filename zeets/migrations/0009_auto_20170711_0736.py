# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 07:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zeets', '0008_auto_20170711_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zeet',
            name='users_like',
        ),
        migrations.AddField(
            model_name='zeet',
            name='likes',
            field=models.ManyToManyField(blank=True, default=0, related_name='zeets_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
