'''
'''
import database
import oauth2
import simplejson as json
from twitter_utils import consumer


class User():
	''''''
	@classmethod
	def load_from_db_by_screen_name(cls, screen_name):
		''''''
		user_data = None
		with database.CursorFromConnectionFromPool() as cursor:
			cursor.execute('SELECT * FROM users WHERE screen_name = %s',
				(screen_name,))
			user_data = cursor.fetchone()

		return cls(screen_name=user_data[1], oauth_token=user_data[2],
				   oauth_token_secret=user_data[3], uid=user_data[0]) \
			   if user_data else None

	def __init__(self, screen_name, oauth_token,
				 oauth_token_secret, uid):
		self.screen_name = screen_name
		self.oauth_token = oauth_token
		self.oauth_token_secret = oauth_token_secret
		self.uid = uid

	def __repr__(self):
		return '<User {}>'.format(self.screen_name)

	def save_to_db(self):
		'''Using `with` statements to insert the appropriate data'''
		with database.CursorFromConnectionFromPool() as cursor:
			cursor.execute('INSERT INTO users (screen_name, '
				'oauth_token, oauth_token_secret) '
				' VALUES (%s, %s, %s)', (self.screen_name,
					self.oauth_token, self.oauth_token_secret))

	def twitter_request(self, uri, verb='GET'):
		# create an authorized token object to perform API calls
		authorized_token = oauth2.Token(
			self.oauth_token, self.oauth_token_secret)
		authorized_client = oauth2.Client(consumer, authorized_token)

		# make Twitter API calls!
		response, content = authorized_client.request(uri, verb)
		if response.status != 200:
			print('An error occurred searching Twitter')

		return json.loads(content.decode('utf-8'))
