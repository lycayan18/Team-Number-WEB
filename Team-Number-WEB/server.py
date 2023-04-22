from os import environ, path
from os.path import join, dirname, realpath
import random

#from dotenv import load_dotenv
from flask import Flask, render_template, redirect, abort, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.utils import secure_filename


from data import db_session
from data.users import User
from data.template_text import HomePage, Google, Yandex, OpenAI, Comment
from forms.register import RegisterForm
from forms.login import LoginForm
from forms.admin import EditingForm
from helpers.password_correct import password_correct
from helpers.name_correct import name_correct

#load_dotenv()
app = Flask(__name__)
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/img/')
app.config['SECRET_KEY'] = "123"#environ.get("KEY_APP")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def home():
    db_sess = db_session.create_session()
    text = db_sess.query(HomePage).all()
    home_text = [
        {'title': '',
         'description': '',
         'img': ''},

        {'title': '',
         'description': '',
         'img': ''},

        {'title': '',
         'description': '',
         'img': ''}
    ]

    for i in range(len(home_text)):
        home_text[i]['title'] = text[i].title
        home_text[i]['description'] = text[i].description
        home_text[i]['img'] = text[i].img
    return render_template("home_page.html", home_text=home_text)


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


@app.route('/<company>/achievements')
def achievements(company):
    if company == "google":
        company_table = Google
    elif company == "yandex":
        company_table = Yandex
    else:
        company_table = OpenAI
    db_sess = db_session.create_session()
    text = db_sess.query(company_table).filter(company_table.key_appointments == 1).all()
    list_data = []
    for i in text:
        list_data.append((i.title, i.description, i.img, i.color, i.id))
    return render_template(f'company_template.html', list_data=list_data, company=company, chapter="achievements")


@app.route('/<company>/developers')
def developers(company):
    if company == "google":
        company_table = Google
    elif company == "yandex":
        company_table = Yandex
    else:
        company_table = OpenAI
    db_sess = db_session.create_session()
    text = db_sess.query(company_table).filter(company_table.key_appointments == 2).all()
    list_data = []
    for i in text:
        list_data.append((i.title, i.description, i.img, i.color))
    return render_template(f'company_template.html', list_data=list_data, company=company, chapter="developers")


@app.route('/<company>/history')
def history(company):
    if company == "google":
        company_table = Google
    elif company == "yandex":
        company_table = Yandex
    else:
        company_table = OpenAI
    db_sess = db_session.create_session()
    text = db_sess.query(company_table).filter(company_table.key_appointments == 3).all()
    list_data = []
    for i in text:
        list_data.append((i.title, i.description, i.img, i.color))
    return render_template(f'company_template.html', list_data=list_data, company=company, chapter="histoty")


@app.route("/add_text/<company>/<chapter>", methods=['GET', 'POST'])
def add_text(company, chapter):
    form = EditingForm()
    if company == "google":
        company_table = Google()
    elif company == "yandex":
        company_table = Yandex()
    else:
        company_table = OpenAI()

    if chapter == "achievements":
        key_appointments_company = 1
    elif chapter == "developers":
        key_appointments_company = 2
    else:
        key_appointments_company = 3
    company_info = company_table
    if request.method == "POST":
        file = request.files['file']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], f'{company}/{filename}'))
            company_info.img = f'/static/img/{company}/{file.filename}'
        else:
            company_info.img = f'/static/img/no_image.jpeg'
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        company_info = company_table
        company_info.title = form.title.data
        company_info.description = form.content.data
        company_info.key_appointments = key_appointments_company
        company_info.color = random.choice(["media_text_block1`", "media_text_block2", "media_text_block3"])
        db_sess.add(company_info)
        db_sess.commit()
        return redirect('/')

    return render_template("admin_panel.html", form=form, title="Добавление информации")


@app.route('/editing_text/<company>/<int:id>', methods=['GET', 'POST'])
@login_required
def editing_text(company, id):
    form = EditingForm()
    if company == "google":
        company_table = Google
    elif company == "yandex":
        company_table = Yandex
    else:
        company_table = OpenAI
    db_sess = db_session.create_session()
    text = db_sess.query(company_table).filter(company_table.id == id).first()
    if request.method == "GET":
        if text:
            form.title.data = text.title
            form.content.data = text.description
        else:
            abort(404)
    if form.validate_on_submit():
        if text:
            text.title = form.title.data
            text.description = form.content.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template("admin_panel.html", form=form, title="Изменение информации")


@app.route('/delete_text/<company>/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_text(company, id):
    if company == "google":
        company_table = Google
    elif company == "yandex":
        company_table = Yandex
    else:
        company_table = OpenAI
    db_sess = db_session.create_session()
    text = db_sess.query(company_table).filter(company_table.id == id).first()
    if text:
        db_sess.delete(text)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


comments = []


@app.route('/comments', methods=['GET'])
def get_comments():
    global comments
    db_sess = db_session.create_session()
    users = db_sess.query(Comment)
    users_dict = [user.__dict__ for user in users]
    for i in range(len(users_dict)):
        comment = {
            'name': users_dict[i]['name'],
            'body': users_dict[i]['body'],
            'time': users_dict[i]['time']
        }
        comments.append(comment)
    all_comment = comments
    comments = []
    return render_template('comment.html', comments=all_comment)


@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    try:
        db_sess = db_session.create_session()
        """
        db_sess = db_session.create_session()
        users = db_sess.query(Comment)
        users_dict = [user.__dict__ for user in users]
        for i in range(len(users_dict)):
            comment = {
                'name': users_dict[i]['name'],
                'body': users_dict[i]['body'],
                'time': users_dict[i]['time']
            }
            comments.append(comment)"""
        comment = {
            'name': data[0]['name'],
            'body': data[0]['body'],
            'time': data[0]['time']
        }
        coment = Comment()
        coment.time = comment['time']
        coment.body = comment['body']
        coment.name = comment['name']
        db_sess.add(coment)
        db_sess.commit()
        comment = {}
        response = {
            'success': True,
            'message': 'Комментарий успешно добавлен'
        }
        return jsonify(response)
    except IndexError:
        return ""


def main():
    db_session.global_init("db/database.db")


if __name__ == '__main__':
    main()
    app.run()
