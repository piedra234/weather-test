from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.citySerializer import CitySerializer
from .querysets.cityQuery import CityQuery
from .management.cityJob import CityJob
from .management.scheduler import scheduler
from .management.exampleJobs import tick,toc # TODO: Delete
# Create your views here.

class CityAPI (APIView):
    """
    API to gets city weather by name and country code
    Parameters:
      city (str): Name
      country (str): 2 Letters code
	Returns: 
      City (Json)"""
    
    def get(self, request, *args, **kwargs):
        if ('city' in request.GET) and ('country' in request.GET):
            city_name= request.GET['city']
            country=request.GET['country'][:2]
            city_query = CityQuery()
            city = city_query.get_city(city_name.lower(), country.upper())
            if city is not None:
                city_query.save_city(city)
                city_serializer = CitySerializer()
                city_serializer = city_serializer.serialize(city)
                return Response(city_serializer)
            else:
                city_serializer = {'cod':'404','message':'City not found'}
                return Response(city_serializer, status=status.HTTP_404_NOT_FOUND)
        else:
            city_serializer = {'cod':'400','message':'Bad Request'}
            return Response(city_serializer, status=status.HTTP_400_BAD_REQUEST)
    
class SchedulerAPI (APIView):
    """
    API to adding a scheduled job that will perform a regular check (every 1 hour) of a city
    Parameters:
      city (str): Name
      country (str): 2 Letters code
	Returns: 
      Code: 202 Accepted 
    """
        
    def put(self, request, *args, **kwargs):
        if ('city' in request.data) and ('country' in request.data):
            city_name= (request.data['city']).lower()
            country=(request.data['country'][:2]).upper()
            city_query = CityQuery()
            city = city_query.get_city(city_name, country)
            if city is not None:
                payload = [city_query,city_name, country]
                city_jobs = CityJob()
                scheduler.add_job(func=city_jobs.add_cityJob, trigger='interval', args=payload, seconds=3600)
                city_serializer = {'cod':'202','message':'Schedule Added'}
                return Response(city_serializer, status=status.HTTP_202_ACCEPTED)
            else:
                city_serializer = {'cod':'404','message':'City not found'}
                return Response(city_serializer, status=status.HTTP_404_NOT_FOUND)
        else:
            city_serializer = {'cod':'400','message':'Bad Request'}
            return Response(city_serializer, status=status.HTTP_400_BAD_REQUEST)


