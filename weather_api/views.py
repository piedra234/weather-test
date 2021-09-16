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
    API to gets city weather by name and country code
    Parameters:
      city (str): Name
      country (str): 2 Letters code
	Returns: 
      City (Json)"""
    
    #def get(self, request, city, country, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        if ('city' in request.GET) and ('country' in request.GET):
            city= request.GET['city']
            country=request.GET['country'][:2]
            city_data = CityQuery()
            obj_city = city_data.get_city(city.capitalize(), country.upper())
            if obj_city is not None:
                city_serializer = CitySerializer()
                obj_city_serializer = city_serializer.serialize(obj_city)
                return Response(obj_city_serializer)
            else:
                obj_city_serializer = {'cod':'404','message':'City not found'}
                return Response(obj_city_serializer, status=404)
        else:
            obj_city_serializer = {'cod':'400','message':'Bad Request'}
            return Response(obj_city_serializer, status=400)