from flask import Blueprint

bp = Blueprint('rl', __name__)

from app.rl import routes
