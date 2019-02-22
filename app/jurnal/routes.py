from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
        jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.jurnal import bp
from app.models import Coa


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('jurnal/index.html', title='Home')


@bp.route('/coa', methods=['GET'])
@login_required
def coa():
    coa = Coa.query.all()
    return render_template('jurnal/coa.html', title='Coa')
