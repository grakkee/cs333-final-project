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

    def test_order_computer(self):
        o = OrderComputer()
        self.assertTrue(o.order())
    
    def test_order_ticker(self):
        o = OrderTicket(1)
        self.assertTrue(o.order())
    
    def test_payment_cash(self):
        p = PaymentCash()
        self.assertTrue(p.pay())
    
    def test_payment_card(self):
        p = PaymentCard()
        self.assertTrue(p.pay())
    
    def test_kiosk(self):
        k = Kiosk()
        self.assertTrue(k.order())
        self.assertTrue(k.pay())
    
    def test_store(self):
        s = Store()
        self.assertTrue(s.order())
        self.assertTrue(s.pay())

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

    def test_kiosk_with_order_behavior(self):
        s = Kiosk()
        self.assertIsInstance(s.order_behavior, OrderBehaviorInterface)
        self.assertIsInstance(s.order_behavior, OrderTicket)
        self.assertNotIsInstance(s.order_behavior, OrderComputer)
    
    def test_kiosk_with_payment_behavior(self):
        s = Kiosk()
        self.assertIsInstance(s.payment_behavior, PaymentBehaviorInterface)
        self.assertIsInstance(s.payment_behavior, PaymentCash)
        self.assertNotIsInstance(s.payment_behavior, PaymentCard)
    
    def test_store_with_order_behavior(self):
        s = Store()
        self.assertIsInstance(s.order_behavior, OrderBehaviorInterface)
        self.assertIsInstance(s.order_behavior, OrderComputer)
        self.assertNotIsInstance(s.order_behavior, OrderTicket)
    
    def test_store_with_payment_behavior(self):
        s = Store()
        self.assertIsInstance(s.payment_behavior, PaymentBehaviorInterface)
        self.assertIsInstance(s.payment_behavior, PaymentCard)
        self.assertNotIsInstance(s.payment_behavior, PaymentCash)