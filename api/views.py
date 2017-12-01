# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
def temperature_list(request):
	data = Temperature.objects.all()
	return render(request, 'temperature_list.html', {'data': data})

