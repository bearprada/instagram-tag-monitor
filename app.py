import bottle
from os import environ
from bottle import route, post, run, request, view
from instagram import client, subscriptions

bottle.debug(True)

CONFIG = {
    'client_id': '27e229137db647e7a4af91f1d1ba6105',
    'client_secret': 'f8900228cca14a72a41fbd2a02d9f0f8',
    'redirect_uri': 'http://instacerberus.herokuapp.com/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

def process_tag_update(update):
    print update

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)

@route('/test')
@view('index')
def test():
    return dict()

@route('/')
def home():
    try:
        url = unauthenticated_api.get_authorize_url(scope=["likes" , "comments"])
        return '<a href="%s">Connect with Instagram</a>' % url
    except Exception, e:
        print e

@route('/oauth_callback')
@view('index')
def on_callback():
    code = request.GET.get("code")
    if not code:
        return 'Missing code'
    try:
        access_token = unauthenticated_api.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'
        api = client.InstagramAPI(access_token=access_token[0])
        tag = api.tag(tag_name='piccollage')
        return dict(count=tag.media_count, token=access_token[0])
    except Exception, e:
        print e

@route('/realtime_callback')
@post('/realtime_callback')
def on_realtime_callback():
    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    verify_token = request.GET.get("hub.verify_token")
    if challenge:
        return challenge
    else:
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            print "Signature mismatch"

run(host='0.0.0.0',  port=int(environ.get("PORT", 5000)), reloader=True)
