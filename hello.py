from contractvmd.dapplang import *

NAME 		= 'helloworld'
VERSION 	= 5
DESCRIPTION	= 'Hello dapp'
AUTHORS 	= ['Davide Gessa <gessadavide@gmail.com>']

# This dapp is compatible with previous helloworld with a version greater than 2
COMPATIBILITY 	= lambda v: v > 2


@dapp
class Hello ():
	@init
	def init (self):
		self.state.init ('names', {})

	@query
	def getNames (self):
		return self.state['names']


	@query
	def getName (self, name):
		return self.state['names'][name]

	@validateQuery ('getName')
	def getNameValidate (self, name, value):
		return (self.state['names'][name] == value)


	@update (0x01)
	def hello (self, name):
		name = name.lower ()

		if name in self.state ['names']:
			self.state ['names']['name'] += 1
		else:
			self.state ['names']['name'] = 1

