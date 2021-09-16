from django.test import TestCase
from weather_api.models.city import City

# Create your tests here.
class CityClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        bog_res = {"coord":{"lon":-74.0817,"lat":4.6097},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":284.24,"feels_like":283.83,"temp_min":284.24,"temp_max":284.24,"pressure":1020,"humidity":93,"sea_level":1020,"grnd_level":754},"visibility":6797,"wind":{"speed":1.51,"deg":119,"gust":2.19},"clouds":{"all":100},"dt":1631752526,"sys":{"country":"CO","sunrise":1631702838,"sunset":1631746549},"timezone":-18000,"id":3688689,"name":"Bogota","cod":200}
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
                        bog_res['id'],
                        bog_res['name'],
                        bog_res['cod'])
        cal_res = {"coord":{"lon":-76.5225,"lat":3.4372},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":297.15,"feels_like":297.51,"temp_min":297.15,"temp_max":297.15,"pressure":1014,"humidity":73},"visibility":10000,"wind":{"speed":2.57,"deg":0},"clouds":{"all":40},"dt":1631752638,"sys":{"type":1,"id":8590,"country":"CO","sunrise":1631703438,"sunset":1631747121},"timezone":-18000,"id":3687925,"name":"Santiago de Cali","cod":200}
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
                    cal_res['id'],
                    cal_res['name'],
                    cal_res['cod'])
        

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
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
        """Cities"""
        bog_res = {"coord":{"lon":-74.0817,"lat":4.6097},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":284.24,"feels_like":283.83,"temp_min":284.24,"temp_max":284.24,"pressure":1020,"humidity":93,"sea_level":1020,"grnd_level":754},"visibility":6797,"wind":{"speed":1.51,"deg":119,"gust":2.19},"clouds":{"all":100},"dt":1631752526,"sys":{"country":"CO","sunrise":1631702838,"sunset":1631746549},"timezone":-18000,"id":3688689,"name":"Bogota","cod":200}
        self.assertEqual(self.bogota.base, bog_res['base'])

    def test_city_compass(self):
        """Compass wind direction"""
        self.assertEqual(self.bogota.compass, 'east-southeast')
        self.assertNotEqual(self.cali.compass, 'west')
        self.london.wind['deg'] = 0
        self.london.compass = self.london.get_compass_direction()
        self.assertEqual(self.london.compass, 'north')
    
    def test_city_beaufort(self):
        """Beaufort scale"""
        self.assertEqual(self.bogota.wind_beaufort, 'Light air')
        self.assertNotEqual(self.cali.wind_beaufort, 'Light air')
        self.assertEqual(self.cali.wind_beaufort, 'west')