import unittest
from order_computer import OrderComputer

class TestUnits(unittest.TestCase):
    def test_order(self):
        o = OrderComputer()

        self.assertTrue(o.order())