from math import radians, sin, cos, asin, sqrt, acos

EARTH_RADIUS = 6378


class Location:

    def __init__(self, lat, long):
        self.lat = float(lat)
        self.long = float(long)

    def to_radians(self):
        return map(radians, [self.lat, self.long])

    def distance_to(self, location):
        lat1, long1 = self.to_radians()
        lat2, long2 = location.to_radians()

        delta_long = max(long1, long2) - min(long1, long2)

        sines = sin(lat1) * sin(lat2)
        cosines = cos(lat1) * cos(lat2) * cos(delta_long)

        central_angle = acos(sines + cosines)
        distance = EARTH_RADIUS * central_angle
        return round(distance, 5)
