# Импорт необходимых модулей
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Указываем URI базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Секретный ключ для защиты сессии
app.config['SECRET_KEY'] = 'secret_key'
# Отключаем отслеживание изменений объектов (Track modifications)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализируем SQLAlchemy с использованием экземпляра приложения в качестве контекста
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Создаем таблицы в базе данных, если они не существуют
with app.app_context():
    db.create_all()
# Определение маршрута для главной страницы
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")
# Определение маршрута для страницы "About"
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signup', methods=['GET', 'POST']) # Обработчик запроса для пути "/signup"
def signup():
    if request.method == 'POST': # Если запрос отправлен методом POST
        username = request.form['username'] # Получение имени пользователя из формы
        password = request.form['password'] # Получение пароля из формы
        confirm_password = request.form['confirm_password'] # Получение подтверждения пароля из формы

        if password != confirm_password: # Если пароль и подтверждение пароля не совпадают
            flash('Пароли не совпадают.', 'ошибка')
        elif User.query.filter_by(username=username).first():  # Если имя пользователя уже существует в базе данных
            flash('Имя пользователя уже существует.', 'ошибка')
        else:
            new_user = User(username=username, password=password) # Создание нового объекта пользователя
            db.session.add(new_user)
            db.session.commit()
            flash("Вы успешно зарегистрировались!", "успех")
            return redirect('/login') # Перенаправление пользователя на страницу входа


    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST']) # Обработчик запроса для пути "/login"
def login():
    if request.method == 'POST': # Если запрос отправлен методом POST
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first() # Проверка имени пользователя и пароля
        if user:
            flash("Вы успешно вошли в систему!", "успех")
            return redirect('/test')
        else:
            flash('Неверное имя пользователя или пароль.', 'ошибка')

    return render_template("login.html")

@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True) # Запуск приложения в режиме отладки
