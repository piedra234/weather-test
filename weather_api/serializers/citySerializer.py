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
                'coord' : f"{city.coord}",
                'weather' : f"{city.weather}",
                'base' : f"{city.base}",
                'main' : f"{city.main}",
                'visibility' : f"{city.visibility}",
                'wind' : f"{city.wind}",
                'clouds' : f"{city.clouds}",
                'dt' : f"{city.dt}",
                'sys' : f"{city.sys}",
                'timezone' : f"{city.timezone}",
                'id_city' : f"{city.id}", #Change
                'name' : f"{city.name}",
                'cod' : f"{city.cod}",
        }
        return city_serialized
