# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeets', '0003_auto_20170706_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/images/'),
        ),
    ]
