from payment_behavior import PaymentBehaviorInterface

class PaymentCard(PaymentBehaviorInterface):
	def pay(self):
		print("Paying with card")

		print("purchase successful")

		return True