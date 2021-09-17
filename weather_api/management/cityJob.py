from weather_api.querysets.cityQuery import CityQuery

class CityJob():

    def add_cityJob(self, city_query, city_name, country):
        city = city_query.renew_city(city_name, country)
        if city is not None:
            city_query.save_city(city)

