
from flask import Flask 
from flask_cors import CORS
import middleware as middleware

app = Flask(__name__)
# Include middleware
app.wsgi_app = middleware.Middleware(app.wsgi_app)
# Fix for CORS header issue in flas
CORS(app)

from app.admin.views import mod

app.register_blueprint(admin.views.mod, url_prefix='/admin')