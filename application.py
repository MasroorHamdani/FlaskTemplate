# -*- encoding: utf-8 -*-
"""
Python Aplication Template
"""

import os
import flask

application = flask.Flask(__name__)
#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	print("Started...")
	application.run(debug = False)
