from weather_api.models.city import City
import requests

class CityQuery():
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032"

    def get_city(self, location, country_name):
        url = self.url
        city_json = (requests.get(url.format(city = location, country = country_name))).json()
        if 'name' in city_json.keys():
            data = City(city_json['coord'],
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
            return data
        else:
            return None



