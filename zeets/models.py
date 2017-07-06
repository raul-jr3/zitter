# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Zeet(models.Model):
	zeeter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'zeets_created')
	body = models.CharField(max_length = 140, help_text = "140 characters only :P")
	created = models.DateTimeField(auto_now = True)
	image = models.ImageField(blank = True, upload_to = '%Y/%m/%d/images/')
	users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.created 

class Comment(models.Model):
	zeet = models.ForeignKey(Zeet, related_name = 'comments')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'commented')
	body = models.CharField(max_length = 350, help_text = "350 characters only")
	photo = models.ImageField(blank = True, upload_to = "%Y/%m/%d/images/")
	created = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return "{} commented on {}".format(self.user, self.zeet)