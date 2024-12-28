import warnings
warnings.filterwarnings('ignore') 

from City import City
from Weather import Weather

city = input("City: ")
countrycode = input("Country code: ")

if city != "" and countrycode != "":
    city = City(city, countrycode)
    if city.valid_country == True:
        coordinates = city.get_coordinates()
        if 'lat' in coordinates and 'lon' in coordinates:
            weather = Weather(coordinates).get_weather()
            print(weather)
        else:
            print("No coordinates found for City: " + city + ", Country: " + countrycode)
    else:
        print("No country found for country code: " + countrycode)
else:
    print("Please provide City and Country code to check weather.")