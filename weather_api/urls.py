from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^weather$', views.CityAPI.as_view(), name="weather"),
    url(r'^scheduler/weather', views.SchedulerAPI.as_view(), name="scheduler"),
]
