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