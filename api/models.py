# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Temperature(models.Model):
	time = models.CharField(max_length=200)
	celsius = models.CharField(max_length=200)

	def __self__(self):
		return self.time

	def __unicode__(self):
		return self.time

	class Meta:
		verbose_name_plural = "temperature"

	class JSONAPIMeta:
		resource_name = "temperature"

class TemperatureAdmin(admin.ModelAdmin):
	list_display = ('time','celsius')

