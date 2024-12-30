import warnings
warnings.filterwarnings('ignore') 

from City import City
from Weather import Weather

cityname = input("City: ")
countrycode = input("Country code: ")

if cityname != "" and countrycode != "":
    city = City(cityname, countrycode.upper())
    if city.valid_country == True:
        coordinates = city.get_coordinates()
        if 'lat' in coordinates and 'lon' in coordinates:
            weather = Weather(coordinates).get_weather()
            print(weather)
        else:
            print("No coordinates found for City: " + cityname + ", Country: " + countrycode)
    else:
        print("No country found for country code: " + countrycode)
else:
    print("Please provide City and Country code to check weather.")