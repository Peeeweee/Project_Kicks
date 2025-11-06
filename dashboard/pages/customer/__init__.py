from flask import Blueprint

bp = Blueprint('customer', __name__, url_prefix='/customer')

from . import routes