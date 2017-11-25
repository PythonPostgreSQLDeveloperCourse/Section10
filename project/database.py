import psycopg2
from psycopg2 import pool


class Database():
	__connection_pool = None

	@staticmethod
	def initialise(**kwargs):
		Database.__connection_pool = pool.SimpleConnectionPool(**kwargs)

	@classmethod
	def get_connection(cls):
		return cls.__connection_pool.getconn()

	@classmethod
	def put_connection(cls, connection):
		cls.__connection_pool.putconn(connection)

	@classmethod
	def close_all_connections(cls):
		Database.__connection_pool.closeall()


class CursorFromConnectionFromPool():
	def __init__(self):
		self.connection = None
		self.cursor = None

	def __enter__(self):
		self.connection = Database.get_connection()
		self.cursor = self.connection.cursor()
		return self.cursor

	def __exit__(self, *exc_info):
		exc_type, exc_val, exc_traceback = exc_info
		if exc_val is not None:
			self.connection.rollback()
		else:
			self.cursor.close()
			self.connection.commit()
		Database.put_connection(self.connection)
