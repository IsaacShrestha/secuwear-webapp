from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.temperature_list, name='temperature_list'),
]