import unittest
from account import Account

class TestAccount(unittest.TestCase):
	def setUp(self):
		pass
	
	def testWithSufficientFunds(self):
		account = Account(10)
		amount = account.debit(4)
		self.assertEqual(amount, 4)
	
	def testWithInsufficientFunds(self):
		account = Account(10)
		amount = account.debit(12)
		self.assertEqual(amount, 10)	

if __name__ == '__main__':
    unittest.main()
	
	
