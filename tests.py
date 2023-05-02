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
        t = OrderComputer()
        self.assertIsInstance(t, OrderComputer)
        self.assertIsInstance(t, OrderBehaviorInterface)
        self.assertNotIsInstance(t, OrderTicket)
    
    def test_order_behavior_with_ticket(self):
        t = OrderTicket(1)
        self.assertIsInstance(t, OrderTicket)
        self.assertIsInstance(t, OrderBehaviorInterface)
        self.assertNotIsInstance(t, OrderComputer)
    
    def test_payment_behavior_with_cash(self):
        p = PaymentCash()
        self.assertIsInstance(p, PaymentCash)
        self.assertIsInstance(p, PaymentBehaviorInterface)
        self.assertNotIsInstance(p, PaymentCard)
    
    def test_payment_behavior_with_card(self):
        p = PaymentCard()
        self.assertIsInstance(p, PaymentCard)
        self.assertIsInstance(p, PaymentBehaviorInterface)
        self.assertNotIsInstance(p, PaymentCash)
    
    def test_shaved_ice_shop_with_kiosk(self):
        s = Store()
        self.assertIsInstance(s, Store)
        self.assertIsInstance(s, ShavedIceShop)
        self.assertNotIsInstance(s, Kiosk)
    
    def test_shaved_ice_shop_with_store(self):
        s = Kiosk()
        self.assertIsInstance(s, Kiosk)
        self.assertIsInstance(s, ShavedIceShop)
        self.assertNotIsInstance(s, Store)