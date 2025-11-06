from flask import Blueprint

bp = Blueprint('sales', __name__, url_prefix='/')

from . import routes