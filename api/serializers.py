from rest_framework import serializers
from .models import *


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Temperature
		fields = ('time', 'celsius')

