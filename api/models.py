# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Temperature(models.Model):
	time = models.CharField(max_length=200)
	celsius = models.CharField(max_length=200)

	def __self__(self):
		return self.time

