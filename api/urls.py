from django.conf.urls import url, include
from . import views

from rest_framework import routers


router=routers.DefaultRouter(trailing_slash=False)
router.register(r'temperature', views.TemperatureViewSet)

urlpatterns = [
	#url(r'^$',views.home, name='home'),
	url(r'^temperature_list$',views.temperature_list, name='temperature_list'),
	url(r'^temperature_new$', views.temperature_new, name='temperature_new'),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]