from weather_api.services.city import City
from weather_api.serializers.citySerializer import CityFullSerializer
from weather_api.models.city import CityModel
from django.forms.models import model_to_dict


import requests

class CityQuery():
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032"

    def get_city(self, location, country_name):
        url = self.url
        # add new source model.cityModel
        obj_cityModel = CityModel.objects.filter(name = location).first()
        if obj_cityModel is not None:
            city_json = model_to_dict(obj_cityModel)
            city_json['id']=city_json['id_city']
            del city_json['id_city']
            print(city_json)
            city_json = (requests.get(url.format(city = location, country = country_name))).json()
            print(city_json)
        else:
            print('Nuevo')
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
            #save obj_city to model
            self.update_city(obj_city)
            return obj_city
        else:
            return None

    def update_city(self, city):
        city_saver = CityFullSerializer()
        obj_city_saver = city_saver.serialize(city)
        CityModel.objects.update_or_create(**obj_city_saver)


