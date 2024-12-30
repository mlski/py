import configparser
import os

class GameConf:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.dirname(__file__)+'/gameconfig.ini')