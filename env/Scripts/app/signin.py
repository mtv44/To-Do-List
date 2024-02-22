from flask import Blueprint, render_template, request, redirect
from app.models import User
auth = Blueprint('auth', __name__)
    



@auth.route("/auth", methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user_email = request.form.get('email', "Пусто(", type=str)
        user_login = request.form.get('login', "Пусто(", type=str)
        res = User.query.filter_by(email=user_email, login=user_login).first()
        print(f'email: {user_email}, login: {user_login}')
        print("Результат проверки пользователя:", res)
        if res:
            print('Такой пользователь существует')
            return redirect("/today")
    return render_template("sign_in.html")