# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Zeet(models.Model):
	zeeter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'zeets_created')
	body = models.CharField(max_length = 140)
	created = models.DateTimeField(auto_now = True)
	image = models.ImageField(blank = True, upload_to = '%Y/%m/%d/images/')
	users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.created 