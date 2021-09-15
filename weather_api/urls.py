from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<str:city>/<str:country>', views.CityAPI.as_view(), name="api_weather"),
]
