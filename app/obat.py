'''Sales App
'''
from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Obat

bp = Blueprint('obat', __name__)

@bp.route('/')
@login_required
def index():
    obat = Obat.query.all()
    return render_template('obat/index.html', obat=obat)
