# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170707_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='from_user',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
