from order_behavior import OrderBehavior
from payment_behavior import PaymentBehavior

class ShavedIceShop():
	def __init__(self, ob=None, pb=None):
		self.order_behavior = ob
		self.order_behavior = pb
	
	def order():
		self.order_behavior.order()
	
	def pay():
		self.payment_behavior.pay()