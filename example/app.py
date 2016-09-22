#!/usr/bin/env python

from wsgi_wovn import Middleware

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"<html><body><a href='/test'>Hello WSGI world!</a></body></html>"]

app = Middleware(application, {
        'user_token': 'IRb6-',
        'secret_key': 'secret',
    })

from werkzeug import run_simple
run_simple('0.0.0.0', 8000, app)
