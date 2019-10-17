from functools import wraps
from flask import request, Response

import requests
import json

def authorization_required():
    def _authorization_required(f):
        @wraps(f)
        def __authorization_required(*args, **kwargs):
            # Access passed request value using request - flask's request object
            path = request.path
            url = request.url
            method = request.method
            # just do here everything what you need
            # Add condition if needed and do needful
            # Validate for Authorization.
            is_authorised = False
            # For Unauthorized access return the Response
            if is_authorised:
                result = f(*args, **kwargs)
                return result
            else:
                return Response(json.dumps({'Message' : 'You are not Authorised for this operation'}),
                    status=403, \
                    mimetype="application/json")
        return __authorization_required
    return _authorization_required