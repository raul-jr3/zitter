# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['date_of_birth']
	list_filter = ['date_of_birth']

admin.site.register(Profile, ProfileAdmin)

