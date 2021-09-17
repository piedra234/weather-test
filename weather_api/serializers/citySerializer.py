from weather_api.services.city import City

class CitySerializer():
   
    def serialize(self, city):
        city_serialized = {
                'location_name' : f"{city.name}, {city.sys['country']}",
                'temperature' : f"{int(city.main['temp'] -273.15)} °C",
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


class CityFullSerializer():
   
    def serialize(self, city):
        city_serialized = {
                'coord' : city.coord,
                'weather' : city.weather,
                'base' : city.base,
                'main' : city.main,
                'visibility' : city.visibility,
                'wind' : city.wind,
                'clouds' : city.clouds,
                'dt' : city.dt,
                'sys' : city.sys,
                'timezone' : city.timezone,
                'id_city' : city.id,
                'name' : city.name,
                'cod' : city.cod,
        }
        return city_serialized
