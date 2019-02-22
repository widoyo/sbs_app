from flask import Blueprint

bp = Blueprint('jurnal', __name__)

from app.jurnal import routes
