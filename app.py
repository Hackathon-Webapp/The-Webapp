from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kajlfal afkljfla'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    return render_template('todo.html')

@app.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template('resources.html')

@app.route('/relaxation', methods=['GET', 'POST'])
def relax():
    return render_template('relax.html')

@app.route('/ebooks', methods=['GET', 'POST'])
def ebooks():
    return render_template('ebooks.html')

@app.route('/ebooks6', methods=['GET', 'POST'])
def ebooks6():
    return render_template('ebooks/ebooks6.html')

@app.route('/ebooks7', methods=['GET', 'POST'])
def ebooks7():
    return render_template('ebooks/ebooks7.html')

@app.route('/ebooks8', methods=['GET', 'POST'])
def ebooks8():
    return render_template('ebooks/ebooks8.html')

@app.route('/images', methods=['GET', 'POST'])
def images():
    return render_template('imgs&diagrams.html')

@app.route('/audio', methods=['GET', 'POST'])
def audios():
    return render_template('audios.html')

@app.route('/img_pdf', methods=['GET', 'POST'])
def img_pdf():
    return render_template('img_pdf.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 4:
            flash('Username must be greater than 4 characters!', category='error')
        elif len(password1) < 4:
            flash('Password must be greater than 4 characters!', category='error')
        elif password1 != password2:
            flash('Passwords do not match!', category='error')
        else:
            flash('Account created!', category='success')
    return render_template('sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
