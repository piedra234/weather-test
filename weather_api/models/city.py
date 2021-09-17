from django.db import models
 

class CityModel(models.Model):
    coord = models.JSONField(db_column='coord')
    weather = models.JSONField(db_column='weather')
    base = models.CharField(db_column='base', max_length=200)
    main = models.JSONField(db_column='main')
    visibility = models.IntegerField(db_column='visibility')
    wind = models.JSONField(db_column='wind',)
    clouds = models.JSONField(db_column='clouds')
    dt = models.IntegerField(db_column='dt')
    sys = models.JSONField(db_column='sys')
    timezone = models.IntegerField(db_column='timezone')
    id_city = models.IntegerField(db_column='id_city')
    name = models.CharField(db_column='name', max_length=200)
    cod = models.IntegerField(db_column='cod')
    created_at = models.DateTimeField(db_column='created_at',auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'city'
    
    def __str__(self):
        return self.name


"""
{
    "coord":{"lon":-74.0817,"lat":4.6097},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
    "base":"stations",
    "main":{"temp":285.85,"feels_like":285.19,"temp_min":285.85,"temp_max":285.85,"pressure":1021,"humidity":77,"sea_level":1021,"grnd_level":756},
    "visibility":10000,
    "wind":{"speed":1.41,"deg":124,"gust":2.48},
    "clouds":{"all":61},
    "dt":1631797224,
    "sys":{"country":"CO","sunrise":1631789223,"sunset":1631832920},
    "timezone":-18000,
    "id":3688689,
    "name":"Bogota",
    "cod":200}"""