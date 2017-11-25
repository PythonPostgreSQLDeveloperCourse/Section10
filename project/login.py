import constants
from database import Database
from user import User
from twitter_utils import (get_request_token, get_oauth_verifier, get_access_token)


Database.initialise(minconn=constants.DB_MIN_CONNS, maxconn=constants.DB_MAX_CONNS,
					user=constants.DB_UNAME, password=constants.DB_PASS,
					database=constants.DB_NAME, host=constants.DB_HOST)

email = input('Enter an email address: ').strip()

# check if user access info is saved in our database
user = User.load_from_db_by_email(email)

if not user:
	request_token = get_request_token()
	oauth_verifier = get_oauth_verifier(request_token)
	access_token = get_access_token(request_token, oauth_verifier)
	first_name, last_name = input('Enter your first and last name: ').split(' ', 2)

	# query was successful, save the user access information
	user = User.load_from_db_by_email(email)
	if not user:
		user = User(email, first_name, last_name,
			access_token['oauth_token'],
			access_token['oauth_token_secret'], None)
		user.save_to_db()

content = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=bitcoin+filter:images&count=4')
for tweet in content['statuses']:
	print('User: {} Tweeted: {}'.format(tweet['user']['screen_name'],
		tweet['text'].encode('ascii', 'ignore')))
