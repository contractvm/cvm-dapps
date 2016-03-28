from contractvmd.dapplang import *

NAME 		= 'fifomom'
VERSION 	= 1
DESCRIPTION	= 'First-in first-out decentralized message-oriented middleware'
AUTHORS 	= ['Davide Gessa <gessadavide@gmail.com>']
COMPATIBILITY 	= lambda v: True


@dapp
class FifoMOM ():
	@query
	def get (self, queue):
		return self.state [queue]

	@update (0x01)
	def publish (self, queue, message):
		if not queue in self.state:
			self.state[queue] = []

		self.state[queue].append (message)
