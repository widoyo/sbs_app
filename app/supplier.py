'''Sales App
'''
from flask import Blueprint, render_template, request
from flask_login import login_required
from sqlalchemy import desc

from app.models import Supplier
from app import db

bp = Blueprint('supplier', __name__)

@bp.route('/')
@login_required
def index():
    supplier = Supplier.query.all()
    return render_template('supplier/index.html', supplier=supplier)


@bp.route('/<kodesup>')
@login_required
def show(kodesup):
    supplier = Supplier.query.filter(Supplier.KODESUP == kodesup).first()
    return render_template('supplier/show.html', supplier=supplier)


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        sup = Supplier(NAMA=request.form['nama'], KODESUP=get_last_kode_sup())
        db.session.add(sup)
        db.session.commit()
    return render_template('supplier/add.html')


def get_last_kode_sup():
    last_sup = db.session.query(Supplier).order_by(desc(Supplier.KODESUP)).first()
    return int(last_sup.KODESUP) + 1
