# Python Web and APIs

## Installing Virtualenv

***Sublime***
- install [package control][packageControl]
- read over [build systems doc][buildSystems]

***Useful for Sublime***
- [SublimeREPL][]
- [SublimeCodeIntel][]

***Virtualenv***
- install [virtualenv][]
- install [virtualenvwrapper][]
- (On Windows) install [virtualenvwrapper-win][]

***Optional***
- install [pyvenv][]

***Speed Bumps***

- Setting up and using virtualenv using `virtualenvwrapper-win` in conjunction with Sublime can be a bit confusing
- Not using `virtualenvwrapper-win` AKA `virtualenvwrapper` command and windows CMD prompt can lead to undesired results setting up virtualenv for use inside Sublime.
	+ Option: Use git bash for running virtualenv commands
	+ I found that using Windows CMD prompt and `virtualenvwrapper` command work best
- Project setup that works best for me
	+ create project directory
	+ create requirements.txt in project directory and include `psycopg2==2.7.x.x` (`.x.x` = current version) in its contents
	+ `mkvirtualenv -a S:\Udemy\python-postgresql\section10-python-web-apis\project -r S:\Udemy\python-postgresql\section10-python-web-apis\project\requirements.txt udemy-postgresql-section10`
	+ After setting up [sublime-text-virtualenv][], open the package manager * <kbd>ctrl+shift+,</kbd>, <kbd>p</kbd>, search "Virtualenv: Activate" then select the option `udemy-postgresql-section10`


## Setting Up Twitter

- The App: [Udemy-Learning-Project](https://apps.twitter.com/app/14506613)
- Oauth Flow
	+ [request token][requestToken], [authorize][], [access token][accessToken]
- Methods
	+ search tweets API method


## Sentiment Analysis

- Perform positive/negative [sentiment analysis][sentimentAnalysis] with external NLP web API 


## Sessions

- Cookies are small bits of information stored in the browser and are a way for memory to persist across pages of a domain
- Sessions are server-side storage and are accessed by the client via a session id
- More on [sessions and cookies][cookies]


## CSS Styling

- [bootstrap home page][bootstrap]
- Copy/paste [bootstrap CDN][] into your html documents
- Browse [bootstrap components][] for a better idea of how to incorporate
- [Jinja templates](http://jinja.pocoo.org/)


[sublime-text-virtualenv]: https://github.com/AdrianLC/sublime-text-virtualenv "sublime-text-virtualenv"
[packageControl]: https://sublime.wbond.net/docs/usage "Package Control"
[buildSystems]: http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/reference/build_systems.html "Sublime Text build systems"
[virtualenv]: https://virtualenv.pypa.io/en/latest/ "virtualenv"
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenvwrapper"
[virtualenvwrapper-win]: https://github.com/davidmarble/virtualenvwrapper-win/ "virtualenvwrapper-win"
[pyvenv]: https://docs.python.org/3.3/library/venv.html "pyvenv"
[SublimeREPL]: https://github.com/wuub/SublimeREPL "SublimeREPL"
[SublimeCodeIntel]: http://sublimecodeintel.github.io/SublimeCodeIntel/ "SublimeCodeIntel"

[API keys]: https://apps.twitter.com/app/14506613/keys
[requestToken]: https://developer.twitter.com/en/docs/basics/authentication/api-reference/request_token.html
[authorize]: https://developer.twitter.com/en/docs/basics/authentication/api-reference/authorize
[accessToken]: https://developer.twitter.com/en/docs/basics/authentication/api-reference/access_token
[searchTweets]: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html

[sentimentAnalysis]: http://text-processing.com/docs/sentiment.html "Sentiment Analysis"
[cookies]: http://www.lassosoft.com/Tutorial-Understanding-Cookies-and-Sessions "sessions and cookies"
[bootstrap]: http://getbootstrap.com/
[bootstrap CDN]: http://getbootstrap.com/docs/4.0/getting-started/download/#bootstrap-cdn
[bootstrap components]: http://getbootstrap.com/docs/4.0/components/list-group/