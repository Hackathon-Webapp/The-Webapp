  
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

@views.route('/relaxation')
def relax():
    return render_template('relax.html', user=current_user)

@views.route('/resources')
def resources():
    return render_template('resources.html', user=current_user)

@views.route('/ebooks')
def ebooks():
    return render_template('ebooks.html', user=current_user)

@views.route('/ebooks6')
def ebooks6():
    return render_template('ebooks/ebooks6.html', user=current_user)

@views.route('/ebooks7')
def ebooks7():
    return render_template('ebooks/ebooks7.html', user=current_user)

@views.route('/ebooks8')
def ebooks8():
    return render_template('ebooks/ebooks8.html', user=current_user)

@views.route('/images')
def images():
    return render_template('imgs&diagrams.html', user=current_user)

@views.route('/audio')
def audios():
    return render_template('audios.html', user=current_user)

@views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', user=current_user), 404

@views.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', user=current_user), 500
