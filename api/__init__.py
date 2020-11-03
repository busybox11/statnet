from flask import Blueprint

api = Blueprint('api', __name__)

from . import hello_world
from . import stats