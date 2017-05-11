"""Calculates the distance between two points on the earth.

Requires the latitude and longitude of those points.

Name: Juan Nicolas Sevilla Siasoco
UPI:jsia894
ID:8104859

"""
import math

earth_radius = 6371

#My house located at latitude -36.971360, longitude 174.920
lat1=math.radians (-36.971)
long1=math.radians (174.920)

#Clock Tower of the University of Auckland latitude -36.8502, longitude 174.7692
lat2=math.radians (-36.850)
long2=math.radians (174.769)

distance = 2 * earth_radius * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((long2-long1)/2) ** 2))

print(distance)


