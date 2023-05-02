from order_computer import OrderComputer
from payment_card import PaymentCard
from shaved_ice_shop import ShavedIceShop

class Store(ShavedIceShop):
	def __init__(self):
		self.order_behavior = OrderComputer()
		self.payment_behavior = PaymentCard()

public class Store extends ShavedIce {

	public Store() {
    	orderBehavior = new Order_Computer();
    	paymentBehavior = new Payment_Card();
	}
}