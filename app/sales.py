'''Sales App
'''
from flask import Blueprint, render_template
from flask_login import login_required

from app.models import Sales

bp = Blueprint('sales', __name__)

@bp.route('/')
@login_required
def index():
    sales = Sales.query.all()
    return render_template('sales/index.html', sales=sales)
