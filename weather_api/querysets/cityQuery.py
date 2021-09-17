import os
from weather_api.services.city import City
from weather_api.serializers.citySerializer import CityFullSerializer
from weather_api.models.city import CityModel
from django.forms.models import model_to_dict
from datetime import datetime, timezone
import requests

class CityQuery():
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032"
        self.new_city = True

    def get_city(self, location, country_name):
        url = self.url
        obj_cityModel = CityModel.objects.filter(name__iexact = location, sys__country=country_name).order_by('-created_at').first()
        if obj_cityModel is not None:
            #If city is in database
            now = datetime.now(timezone.utc)
            difference = (now - obj_cityModel.created_at)
            total_seconds = difference.total_seconds()
            if total_seconds<int(os.environ['APICACHE_SECONDS']):
                # load from database
                city_json = model_to_dict(obj_cityModel)
                city_json['id']=city_json['id_city']
                del city_json['id_city']
                self.new_city = False
            else:
                # request data again
                city_json = (requests.get(url.format(city = location, country = country_name))).json()
        else:
            city_json = (requests.get(url.format(city = location, country = country_name))).json()
        if 'name' in city_json.keys():
            obj_city = City(city_json['coord'],
                        city_json['weather'],
                        city_json['base'],
                        city_json['main'],
                        city_json['visibility'],
                        city_json['wind'],
                        city_json['clouds'],
                        city_json['dt'],
                        city_json['sys'],
                        city_json['timezone'],
                        city_json['id'],
                        city_json['name'],
                        city_json['cod'])
            return obj_city
        else:
            return None

    def save_city(self, city):
        city_full = CityFullSerializer()
        obj_city_serializer = city_full.serialize(city)
        if self.new_city:
            CityModel.objects.create(**obj_city_serializer)