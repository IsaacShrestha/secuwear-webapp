# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from .serializers import *


#import from rest_framework
from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status

def home(request):
	return render(request, 'base.html', {})



# Create your views here.
class TemperatureViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	queryset = Temperature.objects.all()
	serializer_class = TemperatureSerializer

	'''
		To POST data from MetaWear App
	'''
	

	'''def create(self, request, *args, **kwargs):
		print "Received request:"
		#time = request.POST.get('time')
		celsius = request.POST.get('celsius')
		#print request.outerObject
		#print time
		print celsius
		return Response(status=status.HTTP_204_NO_CONTENT)
	'''

def temperature_list(request):
	data = Temperature.objects.all()
	return render(request, 'temperature_list.html', {'data': data})

@csrf_exempt
def temperature_new(request):
	if request.method == 'POST':
		form = TemperatureForm(request.POST)
		#print form
		
		if form.is_valid():
			temperature = form.save(commit=False)
			celsius = form.cleaned_data['celsius']
			print celsius
			temperature.save()



			return HttpResponseRedirect('/temperature_list')
	else:
		form = TemperatureForm()
		
	return render(request, 'temperature_edit.html', {'form': form})
   
