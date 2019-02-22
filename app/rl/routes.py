from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
        jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.models import Jurnal, JurnalItem
from app.rl import bp


@bp.route('/', methods=['GET'])
@login_required
def index():
    bulan = request.args.get('bulan', datetime.now().strftime('%Y-%m-%d'))
    return render_template('rl/index.html', title='Rugi/Laba')
