# 
from datetime import datetime, timedelta, timezone
import time

class City():
    def __init__(self, coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod):
        #External api values
        self.coord = coord 
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod
        # Calculated
        self.wind_beaufort = self.get_wind_beaufort()
        self.compass = self.get_compass_direction()
        self.sunrise = self.get_sunrise_local()
        self.sunset = self.get_sunset_local()
        self.requested_time = self.get_requested_time_local()
    
    def get_wind_beaufort(self):
        """
        Converts wind speed to Beaufort scale
        
        Parameters:
            speed (float): Speed in m/s

        Returns:
            beaufort (str): Beaufort string 
        """
        speed = int(self.wind['speed'])
        if speed<0.5:
            return "Calm"
        elif speed<1.5:
            return "Light air"
        elif speed<3.3:
            return "Light breeze"
        elif speed<5.5:
            return "Gentle breeze"
        elif speed<7.9:
            return "Moderate breeze"
        elif speed<10.7:
            return "Fresh breeze"
        elif speed<13.8:
            return "Strong breeze"
        elif speed<17.1:
            return "High wind"
        elif speed<20.7:
            return "Gale"
        elif speed<24.4:
            return "Strong"
        elif speed<28.4:
            return "Storm"
        elif speed<32.6:
            return "Violent storm"
        else:
            return "Hurricane"
    
    def get_compass_direction(self):
        """
        Converts wind direction in angles to text words
        
        Parameters:
            deg (int): Direction in angles

        Returns:
            rose (str): Compass rose string 
        """
        points = ['north','north-northeast','northeast','east-northeast','east','east-southeast','southeast','south-southeast','south','south-southwest','southwest','west-southwest','west','west-northwest','northwest','north-northwest','north']
        deg = int(self.wind['deg'])
        indx = (int ((deg/45)*2) )
        return points[indx]
    
    def get_sunrise_local(self):
        sunrise = int(self.sys['sunrise'])
        #local_tz = timezone(timedelta(seconds=-time.timezone))
        #local_sunrise = (datetime.fromtimestamp(sunrise)).astimezone(local_tz)
        col_tz = timedelta(hours =5)
        local_sunrise = (datetime.fromtimestamp(sunrise)) - col_tz
        return local_sunrise.strftime('%H:%M')

    def get_sunset_local(self):
        sunset = int(self.sys['sunset'])
        #local_tz = timezone(timedelta(seconds=-time.timezone))
        #local_sunset = (datetime.fromtimestamp(sunset)).astimezone(local_tz)
        col_tz = timedelta(hours =5)
        local_sunset = (datetime.fromtimestamp(sunset)) - col_tz
        return local_sunset.strftime('%H:%M')

    def get_requested_time_local(self):
        requested_time = int(self.dt)
        #local_tz = timezone(timedelta(seconds=-time.timezone))
        #local_rtime = (datetime.fromtimestamp(requested_time)).astimezone(local_tz)
        col_tz = timedelta(hours =5)
        local_rtime = (datetime.fromtimestamp(requested_time)) - col_tz
        return local_rtime.strftime('%Y-%m-%d %H:%M:%S')

