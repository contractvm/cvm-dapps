from contractvmd.dapplang import *

NAME 		= 'blockstore'
VERSION 	= 1
DESCRIPTION	= 'key-value decentralized database'
AUTHORS 	= ['Davide Gessa <gessadavide@gmail.com>']
COMPATIBILITY 	= lambda v: True

@dapp
class Blockstore ():
	@query
	def get (self, key):
		if key in self.state:
			return self.state[key]
		else:
			return None

	@update (0x01)
	def set (self, key, value):
		if not key in self.state:
			self.state [key] = value


