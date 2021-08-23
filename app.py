from website import create_app
from flask import render_template
from flask_login import current_user

app = create_app()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
    return render_template('home.html', user=current_user, username=username)


if __name__ == "__main__":
    app.run(debug=True)
