import unittest

from customers_to_invite.location import Location


class TestLocation(unittest.TestCase):

    def test_to_radians(self):
        location = Location(53.3498, -6.2603)
        rad_lat, rad_long = location.to_radians()
        self.assertEqual(rad_lat, 0.93112)
        self.assertEqual(rad_long, -0.10926)

    def test_distance_to(self):
        location = Location(53.3498, -6.2603)
        location2 = Location(53.3493, -6.2607)
        distance = location.distance_to(location2)
        self.assertEqual(distance, 0.06168)
