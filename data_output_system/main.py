from data import db_session
from data.template_text import HomePage, Google, Yandex, OpenAI
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "123"


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
        list_data.append((i.title, i.description, i.img, i.color, i.alignment))
    return render_template(f'company_template.html', list_data=list_data, company=company)


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
        list_data.append((i.title, i.description, i.img, i.color, i.alignment))
    return render_template(f'company_template.html', list_data=list_data, company=company)


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
        list_data.append((i.title, i.description, i.img, i.color, i.alignment))
    return render_template(f'company_template.html', list_data=list_data, company=company)


def main():
    db_session.global_init("db/database.db")


if __name__ == "__main__":
    main()
    app.run(host="127.0.0.1", port=8080)
