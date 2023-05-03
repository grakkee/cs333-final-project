from payment_behavior import PaymentBehaviorInterface

class PaymentCash(PaymentBehaviorInterface):
	def pay(self):
		print("paying with cash")
		print("$5 was given")
			
		return True;