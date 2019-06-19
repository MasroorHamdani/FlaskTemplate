
from flask import Flask 

app = Flask(__name__)

from app.admin.views import mod

app.register_blueprint(admin.views.mod, url_prefix='/admin')