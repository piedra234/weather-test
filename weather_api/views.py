from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.city import City
from .serializers.citySerializer import CitySerializer
from .querysets.cityQuery import CityQuery
# Create your views here.

class CityAPI (APIView):
    """
    API to gets city weather by name and country code.
    Parameters:
		city (str): Name
    country (str): 2 Letters code
	Returns: 
		City (Json).
    """
    def get(self, request, city, country, *args, **kwargs):
        city_data = CityQuery()
        # TODO; Validate input 
        obj_city = city_data.get_city(city.capitalize(), country.upper())
        city_serializer = CitySerializer()
        obj_city_serializer = city_serializer.serialize(obj_city)
        return Response(obj_city_serializer)
