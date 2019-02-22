from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
        jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.penjualan import bp


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('penjualan/index.html', title='Home')
