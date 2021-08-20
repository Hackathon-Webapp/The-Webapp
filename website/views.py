  
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Todo
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/todo', methods=['GET', 'POST'])
@login_required
def todo():
    if request.method == 'POST':
        todo = request.form.get('todo')
        if len(todo) < 1:
            flash('Todo is too short!', category='error')
        else:
            new_todo = Todo(data=todo, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            flash('Todo Added!', category='success')

    return render_template('todo.html', user=current_user)


@views.route('/delete-todo', methods=['POST'])
def delete_note():
    todo = json.loads(request.data)
    todo_id = todo['id']
    todo = Todo.query.get(todo_id)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()
    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)
