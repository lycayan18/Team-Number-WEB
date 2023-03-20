from os import environ


from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


from data import db_session
from data.users import User
from forms.register import RegisterForm
from forms.login import LoginForm
from helpers.password_correct import password_correct
from helpers.name_correct import name_correct


app = Flask(__name__)
app.config['SECRET_KEY'] = environ["APP_KEY"]
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")

        status_password = password_correct(form.password.data)
        if status_password[0] is False:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message=status_password[1]
                                   )

        status_name = name_correct(form.name.data)
        if status_name[0] is False:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message=status_name[1]
                                   )

        user = User(
            name=form.name.data,
            email=form.email.data,
            admin=0
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def main():
    db_session.global_init("db/users.db")
    app.run()


if __name__ == '__main__':
    main()