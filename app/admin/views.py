from flask import Blueprint, Response
import decorator as decorator
import json

mod = Blueprint('admin', __name__)

@mod.route('/')
@decorator.authorization_required()
def index():
    return Response(json.dumps({'Message' : 'Hello World'}),
        status=200, \
        mimetype="application/json")
    # return 'hello world'
