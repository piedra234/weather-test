import os
from weather_api.services.city import City
from weather_api.serializers.citySerializer import CityFullSerializer
from weather_api.models.cityModel import CityModel
from django.forms.models import model_to_dict
from datetime import datetime, timezone
import requests

class CityQuery():
    """In this file 'city' objs from services are named 'obj_city', 'city_name' str is named 'city' to use external API"""
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032" 
        self.new_city = True

    def get_city(self, location, country_name):
        url = self.url
        cityModel = CityModel.objects.filter(name__iexact = location, sys__country=country_name).order_by('-created_at').first()
        if cityModel is not None:
            #If city is in database
            now = datetime.now(timezone.utc)
            difference = (now - cityModel.created_at)
            total_seconds = difference.total_seconds()
            if total_seconds<int(os.environ['APICACHE_SECONDS']):
                # load from database
                city_req_json = model_to_dict(cityModel)
                city_req_json['id']=city_req_json['id_city']
                del city_req_json['id_city']
                self.new_city = False
            else:
                # request data again
                city_req_json = (requests.get(url.format(city = location, country = country_name))).json()
        else:
            city_req_json = (requests.get(url.format(city = location, country = country_name))).json()
        if 'name' in city_req_json.keys():
            obj_city = City(city_req_json['coord'],
                        city_req_json['weather'],
                        city_req_json['base'],
                        city_req_json['main'],
                        city_req_json['visibility'],
                        city_req_json['wind'],
                        city_req_json['clouds'],
                        city_req_json['dt'],
                        city_req_json['sys'],
                        city_req_json['timezone'],
                        city_req_json['id'],
                        city_req_json['name'],
                        city_req_json['cod'])
            return obj_city
        else:
            return None

    def renew_city(self, location, country_name):
        url = self.url
        city_req_json = (requests.get(url.format(city = location, country = country_name))).json()
        if 'name' in city_req_json.keys():
            obj_city = City(city_req_json['coord'],
                        city_req_json['weather'],
                        city_req_json['base'],
                        city_req_json['main'],
                        city_req_json['visibility'],
                        city_req_json['wind'],
                        city_req_json['clouds'],
                        city_req_json['dt'],
                        city_req_json['sys'],
                        city_req_json['timezone'],
                        city_req_json['id'],
                        city_req_json['name'],
                        city_req_json['cod'])
            return obj_city
        else:
            return None

    def save_city(self, obj_city):
        city_full = CityFullSerializer()
        city_serializer = city_full.serialize(obj_city)
        if self.new_city:
            CityModel.objects.create(**city_serializer)