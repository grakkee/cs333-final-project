from order_behavior import OrderBehaviorInterface
import random

class OrderComputer(OrderBehaviorInterface):
	def __init__(self):
		self.orderNumber = random.randint(0,100)
	
	def order(self):
		print("Ordering with the computer")
		print("Your order number is " + str(self.orderNumber))

		return True
