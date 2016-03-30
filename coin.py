from contractvmd.dapplang import *

NAME 		= 'coin'
VERSION 	= 1
DESCRIPTION	= 'Simple coin dapp'
AUTHORS 	= ['Davide Gessa <gessadavide@gmail.com>']

@dapp
class Coin:
	COINBASE = '0x123342'

	@init
	def init (self):
		self.state [COINBASE] = 1000.0

	@query
	def getBalance (self, address):
		return self.state [address]

		
	@update (0x01)
	def send (self, value, to):
		fr = self.message.address

		if not fr in self.state:
			return None

		# Not enough funds
		if self.state[fr] < value:
			return None

		if not to in self.state:
			self.state [to] = 0.0

		self.state [fr] -= value
		self.state [to] += value
