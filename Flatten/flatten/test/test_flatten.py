import unittest
from flatten import flatten


class TestFlatten(unittest.TestCase):

    def test_flatten_nested_list(self):
        nested_list = [[1, 2], 3, [4, 5, [6], [[7, 8]]]]
        self.assertEqual(flatten.flatten(nested_list), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_flatten_unnested_list(self):
        unnested_list = [1, 2, 3]
        self.assertEqual(flatten.flatten(unnested_list), [1, 2, 3])
