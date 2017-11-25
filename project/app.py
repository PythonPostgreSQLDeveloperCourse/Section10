from flask import (Flask, render_template, session,
	redirect, request, url_for, g)
from twitter_utils import (get_request_token, get_oauth_verifier_url,
	get_access_token)
from user import User
import constants
from database import Database
import requests


app = Flask(__name__)
app.secret_key = '1234' # must be defined when using session

Database.initialise(minconn=constants.DB_MIN_CONNS, maxconn=constants.DB_MAX_CONNS,
					user=constants.DB_UNAME, password=constants.DB_PASS,
					database=constants.DB_NAME, host=constants.DB_HOST)
headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0'})


@app.before_request
def load_user():
	if 'screen_name' in session:
		# g is globally available before and during the entire request
		g.user = User.load_from_db_by_screen_name(session['screen_name'])


@app.route('/')  # create a page in the home directory
def homepage():
	# must be dir in project named "templates"
	return render_template('home.html')


@app.route('/login/twitter') # create a new endpoint
def twitter_login():
	# if user already logged in, don't bother redirecting to Twitter
	if 'screen_name' in session:
		return redirect(url_for('profile'))
	request_token = get_request_token()
	# using cookies to save request token
	# data is then shared between sessions and methods
	session['request_token'] = request_token

	# redirect the user to Twitter so they can authorize our app
	return redirect(get_oauth_verifier_url(request_token))


@app.route('/logout') # logout endpoint
def twitter_logout():
	session.clear()
	return redirect(url_for('homepage'))


@app.route('/auth/twitter') # http://127.0.0.1:4995/auth/twitter?oauth_verifier=1234567
def twitter_auth():
	oauth_verifier = request.args.get('oauth_verifier') # query string params
	access_token = get_access_token(session['request_token'], oauth_verifier)

	user = User.load_from_db_by_screen_name(access_token['screen_name'])
	if not user:
		user = User(access_token['screen_name'], access_token['oauth_token'],
			access_token['oauth_token_secret'], None)
	user.save_to_db()

	session['screen_name'] = user.screen_name

	# redirect the user over to the profile page
	# http://127.0.0.1:4995/profile
	return redirect(url_for('profile')) # url_for(method_name)


@app.route('/profile')
def profile():
	# in html the `{{screen_name}}` is replaced
	return render_template('profile.html', user=g.user)


@app.route('/search')
def search():
	# parse custom query parameters
	# e.g. http://127.0.0.1:4995/search?q=lambo+filter:images
	query = request.args.get('q')
	content = g.user.twitter_request(
		# 'https://api.twitter.com/1.1/search/tweets.json?q=bitcoin+filter:images')
		'https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))

	# tweet_texts = ['User: {} Tweeted: {}'.format(tweet['user']['screen_name'],
	# 	tweet['text'].encode('ascii', 'ignore')) for tweet in content['statuses']]

	# sentiment analysis
	tweet_texts = [dict(tweet=tweet['text'], label='neutral') for tweet in content['statuses']]

	for tt in tweet_texts:
		print tt
		r = requests.post('http://text-processing.com/api/sentiment',
			data={'text': tt['tweet']}, headers=headers)
		try:

			json_response = r.json()
		except ValueError:
			print 'JSON encoding failed'
		else:
			label = json_response['label']
			tt['label'] = label

	return render_template('search.html', content=tweet_texts)


app.run(port=4995)