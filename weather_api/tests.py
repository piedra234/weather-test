from django.test import TestCase
from weather_api.services.city import City
from weather_api.models.cityModel import CityModel
from weather_api.querysets import cityQuery
from weather_api.serializers import citySerializer



# Create your tests here.
class CityClass_cityModel(TestCase):
    """This class test services and models"""
    @classmethod
    def setUpTestData(cls):
        print("Test: CityClass_cityModel")
        print("..setUpTestData")
        bog_res = {"coord":{"lon":-74.0817,"lat":4.6097},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":284.24,"feels_like":283.83,"temp_min":284.24,"temp_max":284.24,"pressure":1020,"humidity":93,"sea_level":1020,"grnd_level":754},"visibility":6797,"wind":{"speed":1.51,"deg":119,"gust":2.19},"clouds":{"all":100},"dt":1631752526,"sys":{"country":"CO","sunrise":1631702838,"sunset":1631746549},"timezone":-18000,"id_city":3688689,"name":"Bogota","cod":200}
        cls.bogota = City(bog_res['coord'],
                        bog_res['weather'],
                        bog_res['base'],
                        bog_res['main'],
                        bog_res['visibility'],
                        bog_res['wind'],
                        bog_res['clouds'],
                        bog_res['dt'],
                        bog_res['sys'],
                        bog_res['timezone'],
                        bog_res['id_city'],
                        bog_res['name'],
                        bog_res['cod'])
        cal_res = {"coord":{"lon":-76.5225,"lat":3.4372},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":297.15,"feels_like":297.51,"temp_min":297.15,"temp_max":297.15,"pressure":1014,"humidity":73},"visibility":10000,"wind":{"speed":2.57,"deg":0},"clouds":{"all":40},"dt":1631752638,"sys":{"type":1,"id":8590,"country":"CO","sunrise":1631703438,"sunset":1631747121},"timezone":-18000,"id_city":3687925,"name":"Santiago de Cali","cod":200}
        cls.cali = City(cal_res['coord'],
                    cal_res['weather'],
                    cal_res['base'],
                    cal_res['main'],
                    cal_res['visibility'],
                    cal_res['wind'],
                    cal_res['clouds'],
                    cal_res['dt'],
                    cal_res['sys'],
                    cal_res['timezone'],
                    cal_res['id_city'],
                    cal_res['name'],
                    cal_res['cod'])
        obj_bogota = CityModel.objects.create(**bog_res)
        obj_cali = CityModel.objects.create(**cal_res)

        

    def setUp(self):
        print(".....setUp")
        lon_res = {"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":285.49,"feels_like":285.13,"temp_min":283.34,"temp_max":287.57,"pressure":1017,"humidity":90},"visibility":10000,"wind":{"speed":1.11,"deg":275,"gust":1.15},"clouds":{"all":87},"dt":1631752828,"sys":{"type":2,"id":2019646,"country":"GB","sunrise":1631770630,"sunset":1631816023},"timezone":3600,"id":2643743,"name":"London","cod":200}
        self.london = City(lon_res['coord'],
                        lon_res['weather'],
                        lon_res['base'],
                        lon_res['main'],
                        lon_res['visibility'],
                        lon_res['wind'],
                        lon_res['clouds'],
                        lon_res['dt'],
                        lon_res['sys'],
                        lon_res['timezone'],
                        lon_res['id'],
                        lon_res['name'],
                        lon_res['cod'])

    def test_city(self):
        """test City"""
        print(".........city")
        bog_res = {"coord":{"lon":-74.0817,"lat":4.6097},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":284.24,"feels_like":283.83,"temp_min":284.24,"temp_max":284.24,"pressure":1020,"humidity":93,"sea_level":1020,"grnd_level":754},"visibility":6797,"wind":{"speed":1.51,"deg":119,"gust":2.19},"clouds":{"all":100},"dt":1631752526,"sys":{"country":"CO","sunrise":1631702838,"sunset":1631746549},"timezone":-18000,"id":3688689,"name":"Bogota","cod":200}
        self.assertEqual(self.bogota.base, bog_res['base'])

    def test_city_compass(self):
        """test Compass wind direction"""
        print(".........function compass")
        self.assertEqual(self.bogota.compass, 'east-southeast')
        self.assertNotEqual(self.cali.compass, 'west')
        self.london.wind['deg'] = 0
        self.london.compass = self.london.get_compass_direction()
        self.assertEqual(self.london.compass, 'north')
    
    def test_city_beaufort(self):
        """Beaufort scale"""
        print(".........function beaufort scale")
        self.assertEqual(self.bogota.wind_beaufort, 'Light air')
        self.assertEqual(self.london.wind_beaufort, 'Light air')
        self.assertNotEqual(self.cali.wind_beaufort, 'Light air')

    def test_cityModel(self):
        """Cities in database"""
        print(".........models")
        obj_cityModel = CityModel.objects.filter(name = 'Bogota', sys__country='CO').order_by('-created_at').first()
        self.assertEqual(self.bogota.base, obj_cityModel.base)
        obj_cityModel = CityModel.objects.filter(name = 'Santiago de Cali', sys__country='CO').order_by('-created_at').first()
        self.assertEqual(self.cali.weather, obj_cityModel.weather)
        obj_cityModel = CityModel.objects.filter(name = 'Santiago de Cali', sys__country='CO').order_by('-created_at').first()
        self.assertNotEqual(self.bogota.weather, obj_cityModel.weather)


class CityView(TestCase):
    """This class test views"""
    @classmethod
    def setUpTestData(cls):
        print("Test: integration view")
        print("..setUpTestData")

        bog_res = {"coord":{"lon":-74.0817,"lat":4.6097},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":284.24,"feels_like":283.83,"temp_min":284.24,"temp_max":284.24,"pressure":1020,"humidity":93,"sea_level":1020,"grnd_level":754},"visibility":6797,"wind":{"speed":1.51,"deg":119,"gust":2.19},"clouds":{"all":100},"dt":1631752526,"sys":{"country":"CO","sunrise":1631702838,"sunset":1631746549},"timezone":-18000,"id_city":3688689,"name":"Bogota","cod":200}
        cal_res = {"coord":{"lon":-76.5225,"lat":3.4372},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":297.15,"feels_like":297.51,"temp_min":297.15,"temp_max":297.15,"pressure":1014,"humidity":73},"visibility":10000,"wind":{"speed":2.57,"deg":0},"clouds":{"all":40},"dt":1631752638,"sys":{"type":1,"id":8590,"country":"CO","sunrise":1631703438,"sunset":1631747121},"timezone":-18000,"id_city":3687925,"name":"Santiago de Cali","cod":200}
        obj_bogota = CityModel.objects.create(**bog_res)
        obj_cali = CityModel.objects.create(**cal_res)

    def setUp(self):
        pass

    ### weather endpoint
    def test_weather_city_exists(self):
        print(".........weather ......ok")
        resp = self.client.get('/weather?city=London&country=Gb')
        self.assertEqual(resp.status_code, 200)

    def test_weather_city_non_exists(self):
        print(".........weather ......404")
        resp = self.client.get('/weather?city=London&country=Co')
        self.assertEqual(resp.status_code, 404)

    def test_weather_bad_req(self):
        print(".........weather ......Bad Request")
        resp = self.client.get('/weather?city=London')
        self.assertEqual(resp.status_code, 400)

    def test_weather_from_db(self):
        print(".........weather ......load response")
        resp = self.client.get('/weather?city=Bogota&country=Co')
        resp2 = self.client.get('/weather?city=Bogota&country=Co')
        self.assertEqual(resp.data['requested_time'], resp2.data['requested_time'])


    ### scheduler/weather endpoint
    def test_scheduler_bad_req(self):
        print(".........scheduler ......bad req")
        resp = self.client.put('/scheduler/weather', {"title": "remember to email dave"}, content_type='application/json')
        self.assertEqual(resp.status_code, 400)

    def test_scheduler_no_type(self):
        print(".........scheduler ......no type")
        resp = self.client.put('/scheduler/weather', {"title": "remember to email dave"})
        self.assertEqual(resp.status_code, 415)

    def test_scheduler_non_exists(self):
        print(".........scheduler ......404")
        resp = self.client.put('/scheduler/weather', {"city": "??msterdam", "country": "NL"}, content_type='application/json')
        self.assertEqual(resp.status_code, 404)

    def test_scheduler_ok(self):
        print(".........scheduler ......ok")
        resp = self.client.put('/scheduler/weather', {"city": "Amsterdam", "country": "NL"}, content_type='application/json')
        self.assertEqual(resp.status_code, 202)