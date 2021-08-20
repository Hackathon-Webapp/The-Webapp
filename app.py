from website import create_app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

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
