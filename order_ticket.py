from order_behavior import OrderBehaviorInterface

class OrderTicket(OrderBehaviorInterface):
	def __init__(self, ticketNumber):
		self.ticketNumber = ticketNumber
	
	def order(self):
		print("Ordering with a Ticket")
		print("Ticket Number:  " + str(self.ticketNumber))

		return True