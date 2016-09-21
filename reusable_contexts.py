
class DB:
	def __init__(self, params):
		print('We are in __init__')
		self.params = params
		self.connect()

	def __enter__(self):
		return self

	def __exit__(self):
		print('We are in __exit__')
		self.close()

	def __del__(self):
		print('We are in __del__')
		self.__exit__()
		del(self)

	def connect(self):
		print('We are in connect')
		self.connected = True
		return self.connected

	def close(self):
		print('we are in close')
		self.connected = False
		return self.connected

	def execute(self, param):
		print('TRANSACTION: ', 'We are in execute')
		if self.connected:
			print(param)
			return 'ok'
		else:
			raise Exception('No db connection open!')


def no_transaction():
	print('TESTING WITH NO TRANSACTION')
	conn = DB('connection parameters')

def transaction():
	print('TESTING WITH A TRANSACTION')
	conn = DB('connection parameters')
	conn.execute('a transaction')

def error():
	print('TESTING WITH ERRORS')
	conn = DB('connection parameters')
	conn.execute(Exception + 1)

no_transaction()
transaction()
error()