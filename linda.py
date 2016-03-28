from contractvmd.dapplang import *

NAME 		= 'linda'
VERSION 	= 1
DESCRIPTION	= 'Linda decentralized coordination model'
AUTHORS 	= ['Davide Gessa <gessadavide@gmail.com>']
COMPATIBILITY 	= lambda v: True

@dapp
class Linda ():
	@init
	def init (self):
		self.state ['tuples'] = []

	# The query system allows these query:
	# (,,)			Match a tuple with 3 elements of any types
	# (,%f,)		Match a tuple with 3 elements where the second element is a float (or %s: string, %d: int)
	# ('ciao',,)	Match a tuple with 3 elements where the first element is the string 'ciao'
	def _match (self, t, q):
		q = q.replace ('(', '').replace (')', '').replace (', ', ',').split (',')
		# Length check
		if len (q) != len (t): return False

		i = -1
		for qt in q:
			i += 1

			# Empty string: field existence
			if len (qt) == 0: continue

			# Start with %, typematch
			if qt[0] == '%':
				if qt[1] == 'f' and type (t[i]) == float: continue
				elif qt[1] == 'd' and type (t[i]) == int: continue
				elif qt[1] == 's' and type (t[i]) == str: continue
				else: return False

			# Value match
			else:
				if type(eval (qt)) == type (t[i]) and eval (qt) == t[i]: continue
				else: return False

		return True

	def _query (self, q):
		for t in self.state['tuples']:
			try:
				if self._match (literal_eval (t), q): return t
			except:
				pass

		return None


	@query
	def read (self, q):
		return self._query (q)


	@update (0x01)
	def insert (self, t):
		self.state['tuples'].remove (t)

	@preUpdate ('insert')
	def preInsert (self, q):
		return self._query (q)

	@validateUpdate ('insert')
	def validateInsert (self, q, t):
		# Check if t is a valid result for q (dummy, not implemented)
		return True


	@update (0x02)
	def output (self, tp):
		self.state['tuples'].append (tp)

