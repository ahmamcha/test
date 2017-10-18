class Account:
	def __init__(self, balance):
		self.balance = balance
	
	def debit(self, amount):
		if self.balance < amount:
			amount = self.balance
		self.balance -= amount
		return amount

