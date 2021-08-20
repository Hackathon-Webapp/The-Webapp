  
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


@views.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template('resources.html')

@views.route('/relaxation', methods=['GET', 'POST'])
def relax():
    return render_template('relax.html')

@views.route('/ebooks', methods=['GET', 'POST'])
def ebooks():
    return render_template('ebooks.html')

@views.route('/ebooks6', methods=['GET', 'POST'])
def ebooks6():
    return render_template('ebooks/ebooks6.html')

@views.route('/ebooks7', methods=['GET', 'POST'])
def ebooks7():
    return render_template('ebooks/ebooks7.html')

@views.route('/ebooks8', methods=['GET', 'POST'])
def ebooks8():
    return render_template('ebooks/ebooks8.html')

@views.route('/images', methods=['GET', 'POST'])
def images():
    return render_template('imgs&diagrams.html')

@views.route('/audio', methods=['GET', 'POST'])
def audios():
    return render_template('audios.html')

@views.route('/img_pdf', methods=['GET', 'POST'])
def img_pdf():
    return render_template('img_pdf.html')

@views.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@views.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
