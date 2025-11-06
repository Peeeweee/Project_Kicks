from flask import Blueprint

bp = Blueprint('prediction', __name__, url_prefix='/prediction')

from . import routes