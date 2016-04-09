import webapp2
import json
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Line Bot')

    def post(self):
        req_json = json.loads(self.request.body)
        mid =req_json['result'][0]['content']['from']
        send_message2(mid)
        return 'hello'


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


def send_message2(mid):
    url = 'https://trialbot-api.line.me/v1/events'
    headers = {
        'content-type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': YOUR CHANNEL ID,
        'X-Line-ChannelSecret': 'YOUR CHANNEL SECRET',
        'X-Line-Trusted-User-With-ACL': 'YOUR MID'
    }
    payload = {
        'to': [mid],
        'toChannel': 1383378250,
        'eventType': 138311608800106203,
        'content': {
            'contentType': 1,
            'toType': 1,
            'text': 'Hello'
        }
    }
    params = json.dumps(payload)
    try:
        req = urllib2.Request(url, params, headers)
        res = urllib2.urlopen(req)
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
        print 'Error reason: ', e.read()
        raise Exception(e.reason)
    except URLError, e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
        raise Exception(e.reason)

    print res.read()
