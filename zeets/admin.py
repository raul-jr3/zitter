# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Zeet

class ZeetAdmin(admin.ModelAdmin):
	list_display = ['zeeter', 'created']
	list_filter = ['zeeter']

admin.site.register(Zeet, ZeetAdmin)