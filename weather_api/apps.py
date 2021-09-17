import os
from django.apps import AppConfig


class WeatherApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_api'

    def ready(self):
        from .management import scheduler
        if os.environ['SCHEDULER_AUTOSTART']:
            print('Running scheduler')
            scheduler.start()