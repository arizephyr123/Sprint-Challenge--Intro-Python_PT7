# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv
# import numpy


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name}: ({self.lat}, {self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the
  # `cities` list
    with open('cities.csv') as cities_cvs:
        reader = csv.DictReader(cities_cvs)
        for row in reader:
            cities.append(City(row['city'], float(
                row['lat']), float(row['lng'])))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print((c.name, c.lat, c.lon))

    # STRETCH GOAL!
    #
    # Allow the user to input two points, each specified by latitude and longitude.
    # These points form the corners of a lat/lon square. Pass these latitude and
    # longitude values as parameters to the `cityreader_stretch` function, along
    # with the `cities` list that holds all the City instances from the `cityreader`
    # function. This function should output all the cities that fall within the
    # coordinate square.
    #
    # Be aware that the user could specify either a lower-left/upper-right pair of
    # coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
    # the input data so that it's always one or the other, then search for cities.
    # In the example below, inputting 32, -120 first and then 45, -100 should not
    # change the results of what the `cityreader_stretch` function returns.
    #
    # Example I/O:
    #
    # Enter lat1,lon1: 45,-100
    # Enter lat2,lon2: 32,-120
    # Albuquerque: (35.1055,-106.6476)
    # Riverside: (33.9382,-117.3949)
    # San Diego: (32.8312,-117.1225)
    # Los Angeles: (34.114,-118.4068)
    # Las Vegas: (36.2288,-115.2603)
    # Denver: (39.7621,-104.8759)
    # Phoenix: (33.5722,-112.0891)
    # Tucson: (32.1558,-110.8777)
    # Salt Lake City: (40.7774,-111.9301)

'''
# shorter stretch solution
try:
    lat1, lon1 = input("Enter lat1,lon1: ").split(',')
    lat2, lon2 = input("Enter lat2,lon2: ").split(',')
except ValueError:
    print("Please enter two integer values, one for the lat and one for the lon.")


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    within = []
    lat1, lon1 = float(lat1), float(lon1)
    lat2, lon2 = float(lat2), float(lon2)
    # Normalize
    if lat2 < lat1:
        lat1, lat2 = lat2, lat1  # Swap
    if lon2 < lon1:
        lon1, lon2 = lon2, lon1  # Swap
    # Filter
    for c in cities:
        if c.lat >= lat1 and c.lat <= lat2 and c.lon >= lon1 and c.lon <= lon2:
            within.append(c)
    return within
'''

# TODO Get latitude and longitude values from the user


def get_coords():
    first = input("enter 1st lat, lon seperated by commas:\n").split(',')
    second = input("enter 2nd lat, lon seperated by commas:\n").split(',')

    global lat1
    global lon1
    global lat2
    global lon2

    lat1 = float(first[0])
    lon1 = float(first[1])
    lat2 = float(second[0])
    lon2 = float(second[1])

    return lat1, lon1, lat2, lon2


lat1 = 0
lon1 = 0
lat2 = 0
lon2 = 0

get_coords()


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  # within will hold the cities that fall within the specified region
    within = []

    lats = [lat1, lat2]
    lats_sorted = sorted(lats, key=float)
    lat_min = lats_sorted[0]
    lat_max = lats_sorted[1]

    lons = [lon1, lon2]
    lons_sorted = sorted(lons, key=float)
    lon_min = lons_sorted[0]
    lon_max = lons_sorted[1]

    for city in cities:
        if city.lat > lat_min and city.lat < lat_max and city.lon > lon_min and city.lon < lon_max:
            print(city.name)
            within.append(city)

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    # print(len(within))
    return within


cityreader_stretch(lat1, lon1, lat2, lon2, cities)
