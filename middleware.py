from flask import Request

class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("********middleware")
        request = Request(environ)
        path = request.path
        url = request.url
        method = request.method
        print("path: %s, url: %s, method: %s" % (path, url, method))
        
        return self.app(environ, start_response)