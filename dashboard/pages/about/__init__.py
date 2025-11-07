# /dashboard/pages/about/__init__.py

from flask import Blueprint

bp = Blueprint('about', __name__, url_prefix='/about')

from . import routes
