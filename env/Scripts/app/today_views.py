# today_views.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User
from . import db

today_bp = Blueprint('today', __name__)

@today_bp.route('/today', methods=['GET', 'POST'])
def today():
    if request.method == 'POST':
        task_description = request.form.get('checkboxText')
        new_task = User(task=task_description)
        db.session.add(new_task)
        db.session.commit()

    tasks = User.query.all()

    return render_template('today.html', tasks=tasks)

@today_bp.route('/delete_task/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    task = User.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for('today.today'))
