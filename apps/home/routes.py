from flask import render_template
from flask_login import login_required, current_user

from apps.home import blueprint


@blueprint.route('/')
def index():
    return render_template('home/index.html')


@blueprint.route('/profile')
@login_required
def profile():
    return render_template('home/profile.html', email=current_user.email)
