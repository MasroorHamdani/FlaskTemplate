# FlaskTemplate
Flask App template

#Install python

brew install python3
Set up path
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"

# Test if python is installed
python3

# Install pip
easy_install pip

# Install Virtiwl Environment
python3 -m pip install --user virtualenv

# Create Virtual Environment
python3 -m virtualenv env

# Activate virtual Environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt

Set up env variables
export FLASK_APP=application
export FLASK_ENV=development

# To run the server, enter below command
flask run

# Deactivate virtualenv
deactivate

# For running test cases:
pytest OR

pytest -v
