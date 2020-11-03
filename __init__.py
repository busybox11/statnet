import os
from flask import Flask

app = Flask(__name__, static_url_path='web')

from api import api

app.register_blueprint(api, url_prefix='/api')