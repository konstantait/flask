from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required

from apps import db
from apps.auth import blueprint
from apps.auth.models import Users
from apps.auth.util import verify_pass


@blueprint.route('/login')
def login():
    return render_template('accounts/login.html')


@blueprint.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not verify_pass(password, user.password):
        flash('Incorrect email or password, try again')
        # if user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user)
    return redirect(url_for('home.profile'))


@blueprint.route('/registration')
def registration():
    return render_template('accounts/registration.html')


@blueprint.route('/registration', methods=['POST'])
def registration_post():

    email = request.form.get('email')

    # if this returns a user, then the email already exists in database
    user = Users.query.filter_by(email=email).first()

    # if a user is found, we want to redirect back to signup page so user can try again
    if user:
        flash('E-mail address already exists')
        return redirect(url_for('auth.registration'))

    # else we can create the user
    user = Users(**request.form)

    # add the new user to the database
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
