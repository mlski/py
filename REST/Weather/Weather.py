import requests
import configparser
import os

class Weather:
    def __init__(self, coordinates):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.dirname(__file__)+'/weather.ini')
        
        self.lat = coordinates['lat']
        self.lon = coordinates['lon']
        self.apikey = self.config['api.config']['apikey']
        self.apiurl = self.config['api.config']['apiurl']
        
    def get_weather(self):
        returnmsg = ""
        headers = {
             "x-rapidapi-key": self.apikey
        }
        apiurl = self.apiurl + '?lon=' + str(self.lon) + '&lat=' + str(self.lat)
        req = requests.get(apiurl, headers = headers)
        
        resp = req.json()
        if 'data' in resp:
            returnmsg = "Temperature for {} is {} celsius".format(resp['city_name'], resp['temp'])
        else:
            returnmsg = "No weather for given city found"
            
        return returnmsg
        
        