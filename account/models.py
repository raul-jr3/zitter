# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	photo = models.ImageField(blank = True, upload_to = '%Y/%m/%d/profiles/')
	date_of_birth = models.DateTimeField(blank = True, null = True)
	bio = models.CharField(max_length = 350, help_text = '350 characters only. Make it short ^_^')

	def __str__(self):
		return "profile for {} has been created".format(self.user)

class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name = 'rel_from_set')
	user_to = models.ForeignKey(User, related_name = 'rel_to_set')
	created = models.DateTimeField(auto_now_add = True, db_index = True)
	#following = models.ManyToManyField('self', through = Contact, related_name = 'followers', symmetrical = False)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return "{} follows {}".format(self.user_from, self.user_to)

User.add_to_class('following', models.ManyToManyField('self', through = Contact, related_name = 'followers', symmetrical = False))