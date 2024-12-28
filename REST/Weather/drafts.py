import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__)+'/weather.ini')
print(config['api.config']['apikey'])