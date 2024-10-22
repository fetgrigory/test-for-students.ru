# Import required modules
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# Initialize Flask app
app = Flask(__name__)
# Configure database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define User model for database with id, username, and password


class User(db.Model):
    """AI is creating summary for User

    Args:
        db ([type]): [description]
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Create tables in the database


with app.app_context():
    db.create_all()
# Defining the route for the main page


@app.route('/')
@app.route('/home')
def index():
    """AI is creating summary for index

    Returns:
        [type]: [description]
    """
# Render the home page
    return render_template("index.html")


@app.route('/about')
def about():

    """AI is creating summary for

    Returns:
        [type]: [description]
    """
# Render the about page
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
        # Query database for the user with given credentials
        user = User.query.filter_by(
            username=username,
            password=password
        ).first()
        # If user exists, display success message and redirect
        if user:
            flash("Вы успешно вошли в систему!", "успех")
            return redirect('/test')
        # If credentials are incorrect, display error message
        else:
            flash('Неверное имя пользователя или пароль.', 'ошибка')
        # Render the login page template
    return render_template("login.html")


@app.route('/test')
def test():
    """AI is creating summary for test

    Returns:
        [type]: [description]
    """
    return render_template("test.html")


if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
