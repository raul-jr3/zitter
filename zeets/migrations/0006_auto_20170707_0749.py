# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zeets', '0005_auto_20170707_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='like',
            name='zeet',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]