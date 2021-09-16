from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('<str:city>/<str:country>', views.CityAPI.as_view(), name="api_weather"),
    url(r'^weather$', views.CityAPI.as_view(), name="api_weather"),
]
