

def function():
	raise TypeError('HAHAHAHAHAHAHAS')

class Manager:

	def __init__(self, something):
		self.something = None
		try:
			self.something = something.split()
		except AttributeError:
			print('Connection failed.')
			self.__exit__(AttributeError, something, None)

	def __enter__(self):
		print('IN ENTER: ', self.something)
		function()
		return self

	def printer(self):
		print('IN PRINTER: ', self.something)

	def __exit__(self, exec_type, exec_value, traceback):
		print('EXECTYPE: ', exec_type)
		print('EXECVALUE: ', exec_value)
		print('TRACEBACK: ', traceback)
		print('Exiting...')

with Manager(None) as manager:
	manager.printer()


