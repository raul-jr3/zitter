# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	photo = models.ImageField(blank = True, upload_to = '%Y/%m/%d/profiles/')
	date_of_birth = models.DateTimeField(blank = True, null = True)
	bio = models.CharField(max_length = 350, help_text = '350 characters only. Make it short ^_^')

	def __str__(self):
		return "profile for {} has been created".format(self.user)