from shaved_ice_shop import ShavedIceShop
from order_ticket import OrderTicket
from payment_cash import PaymentCash

class Kiosk(ShavedIceShop):
	def __init__(self):
		self.order_behavior = OrderTicket()
		self.payment_behavior = PaymentCash()
