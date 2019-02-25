'''Sales App
'''
from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Supplier

bp = Blueprint('supplier', __name__)

@bp.route('/')
@login_required
def index():
    supplier = Supplier.query.all()
    return render_template('supplier/index.html', supplier=supplier)
