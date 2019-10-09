from flask import Blueprint
import decorator as decorator

mod = Blueprint('admin', __name__)

@mod.route('/')
@decorator.home_decorator()
def index():
    return 'Hello world!!!'
