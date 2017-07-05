# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 14:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='%Y/%m/%d/profiles/')),
                ('date_of_birth', models.DateTimeField(blank=True)),
                ('bio', models.CharField(help_text='350 characters only. Make it short ^_^', max_length=350)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]