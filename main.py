from flask import Flask, render_template, request, flash, redirect
from database.SQLAlchemy_db import db, User, init_app
# Initialize Flask app
app = Flask(__name__)

# Initialize configurations and SQLAlchemy
init_app(app)

# Create tables in the database if they don't exist
with app.app_context():
    db.create_all()


# Defining the route for the main page
@app.route('/')
# Render the home page
@app.route('/home')
def index():
    """AI is creating summary for index

    Returns:
        [type]: [description]
    """
    return render_template("index.html")


# Render the about page
@app.route('/about')
def about():
    """AI is creating summary for about

    Returns:
        [type]: [description]
    """
    return render_template("about.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """AI is creating summary for signup

    Returns:
        [type]: [description]
    """
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Пароли не совпадают.', 'ошибка')
        # Check if user already exists
        elif User.query.filter_by(username=username).first():
            flash('Имя пользователя уже существует.', 'ошибка')
        else:
            # Create a new user
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Вы успешно зарегистрировались!", "успех")
            return redirect('/login')
        # Render the signup page
    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """AI is creating summary for login

    Returns:
        [type]: [description]
    """
    # Retrieve username and password from form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            flash("Вы успешно вошли в систему!", "успех")
            return redirect('/test')
        else:
            flash('Неверное имя пользователя или пароль.', 'ошибка')
    return render_template("login.html")


@app.route('/test')
def test():
    """AI is creating summary for test

    Returns:
        [type]: [description]
    """
    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)
