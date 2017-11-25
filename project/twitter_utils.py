import oauth2
import constants
import urlparse


# create a consumer (allow Twitter to id the app)
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
	client = oauth2.Client(consumer)

	response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
	if response.status != 200:
		print('An error occurred requesting token from Twitter')

	# parse query string parameter
	return dict(urlparse.parse_qsl(content))


def get_oauth_verifier_url(request_token):
	return '{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token'])


def get_oauth_verifier(request_token):
	'''ask user to input the pin they recieve after granting access to the app'''
	print('Go to the following site in a browser:')
	print(get_oauth_verifier_url())

	# ask user to input the pin they recieve after granting access to the app
	return input('Paste pin code you recieved here: ').strip()


def get_access_token(request_token, oauth_verifier):
	token = oauth2.Token(request_token['oauth_token'],
		request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)

	client = oauth2.Client(consumer, token)

	response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
	if response.status != 200:
		print('An error occurred requesting token from Twitter')

	return dict(urlparse.parse_qsl(content))
