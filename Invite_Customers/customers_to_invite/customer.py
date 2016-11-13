
from location import Location


class Customer:
    def __init__(self, id, name, lat, long):
        self.id = id
        self.name = name
        self.location = Location(lat, long)

    def distance_to_dublin_office(self):
        dublin_office = Location(53.3393, -6.2576841)
        return round(self.location.distance_to(dublin_office), 5)
