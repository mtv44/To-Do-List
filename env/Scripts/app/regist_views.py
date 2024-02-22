from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, User

regist = Blueprint('main', __name__)

@regist.route("/", methods=['GET', 'POST'])
def registration_page():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_login = request.form.get('login')

        existing_user = User.query.filter_by(login=user_login).first()
        if not existing_user:
            new_user = User(email=user_email, login=user_login)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('today'))

    return render_template("registration.html")

