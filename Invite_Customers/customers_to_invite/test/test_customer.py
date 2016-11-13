import unittest

from customers_to_invite.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_distance_to_dublin_office(self):
        customer = Customer('1', 'Jerry Smith', '52.073492', '-1.014696')
        self.assertEqual(customer.distance_to_dublin_office(), 380.54915)
