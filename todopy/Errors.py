"""Errors is file to handling and managing errors inside the app."""

# todopy/Errors.py

class TodoExceptions(Exception) : 
	"""Todo exceptions handler"""
	pass

# Todo database exceptions handler.

# SUCCESS, DIR_ERROR, FILE_ERROR, DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, ID_ERROR
# DataBase, System, JSON

class DataBaseExceptions(TodoExceptions) :
	def __init__(self, error, message) : 
		self.error = error
		self.message = message

	def __str__(self) -> str :
		return f":( Oops; error => {self.error}, message => {self.message}"