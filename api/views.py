# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def temperature_list(request):
	return render(request, 'temperature_list.html')

