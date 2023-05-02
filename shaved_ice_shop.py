from order_behavior import OrderBehaviorInterface
from payment_behavior import PaymentBehaviorInterface

class ShavedIceShop():
	def __init__(self, ob=None, pb=None):
		self.order_behavior = ob
		self.order_behavior = pb
	
	def order(self):
		return self.order_behavior.order()
	
	def pay(self):
		return self.payment_behavior.pay()