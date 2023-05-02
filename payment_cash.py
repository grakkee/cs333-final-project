from payment_behavior import PaymentBehavior

class PaymentCash(PaymentBehavior):
	def pay():
		print("paying with cash")
		t = input("enter total in sale")
		while True:
			a = input("please enter amount given")

			if (a<t):
				print("not sufficient amount")
			else:
				print("Your change is: " + str(a-t))
				break;
		return True;