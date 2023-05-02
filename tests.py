import unittest

#order classes
from order_computer import OrderComputer
from order_ticket import OrderTicket
from order_behavior import OrderBehaviorInterface

#payment classes
from payment_card import PaymentCard
from payment_cash import PaymentCash
from payment_behavior import PaymentBehaviorInterface

#shaved ice classes
from shaved_ice_shop import ShavedIceShop
from kiosk import Kiosk
from store import Store

class TestUnits(unittest.TestCase):

    #
    #
    #unit tests
    #
    #

    def test_order(self):
        o = OrderComputer()

        self.assertTrue(o.order())
    

    #
    #
    # integration tests
    #
    #

    def test_order_behavior_with_computer(self):
        #
    
    def test_order_behavior_with_ticket(self):
        #
    
    def test_payment_behavior_with_cash(self):
        #
    
    def test_payment_behavior_with_card(self):
        #
    
    def test_shaved_ice_shop_with_kiosk(self):
        #
    
    def test_shaved_ice_shop_with_store(self):