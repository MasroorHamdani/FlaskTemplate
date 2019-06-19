from flask import Blueprint
mod = Blueprint('admin', __name__)

@mod.route('/')
def index():
    return 'Hello world!!!'
