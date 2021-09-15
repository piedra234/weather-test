from weather_api.models.city import City

class CitySerializer():
   
    def serialize(self, city):
        city_serialized = {
                'location_name' : f"{city.name}, {city.sys['country']}",
                'temperature' : f"{city.main['temp']} °C",
                'wind' : f"{city.wind_beaufort}, {city.wind['speed']} m/s, {city.compass}",
                'cloudines' : f"{city.weather[0]['description']}",
                'presure' : f"{city.main['pressure']} hpa",
                'humidity' : f"{city.main['humidity']}%",
                'sunrise' : f"{city.sunrise}",
                'sunset' : f"{city.sunset}",
                'geo_coordinates' : f"[{city.coord['lat']:.2f}, {city.coord['lon']:.2f}]",
                'requested_time' : f"{city.requested_time}",
        }
        return city_serialized

"""
json format
{
"location_name": "Bogota, CO",
"temperature": "17 °C",  # TODO: temperatura esta en formato 299.02 es necesario aplicar alguna conversion para llegar a grados centigrados
"wind": Gentle breeze, 3.6 m/s, west-northwest",
"cloudines": "Scattered clouds",
"presure": "1027 hpa",
"humidity": "63%",
"sunrise": "06:07",
"sunset": "18:00",
"geo_coordinates": "[4.61, -74.08]",
"requested_time": "2018-01-09 11:57:00"
}
"""