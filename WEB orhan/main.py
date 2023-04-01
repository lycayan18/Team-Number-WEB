from data import db_session
from data.template_text import User, Google, Openai
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"


@app.route("/yandex")
def yandex_title():
    with open("helpers/text_yandex", "r") as flag:
        flag = flag.read()
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text_yandex.db")) == flag:
        for j in range(3):
            for i in range(3):
                yandex = User()
                yandex.name = f"Достижения_{j}"
                yandex.img = f"static/img/{i}.png"
                db_sess.add(yandex)
        with open("helpers/text_yandex", "w") as flag:
            flag.write("False")
    db_sess.commit()
    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"],\
                                                                           ["История компании"]
    for i in db_session.create_session().query(User):
        if 1 <= i.id <= 3:
            achievements_database.append(i.name)
        elif 4 <= i.id <= 6:
            developers_database.append(i.name)
        else:
            company_history_database.append(i.name)
    return render_template("yandex.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database)


@app.route("/openai")
def openai_title():
    with open("helpers/text_openai", "r") as flag:
        flag = flag.read()
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text_openai.db")) == flag:
        for j in range(3):
            for i in range(3):
                openai = Openai()
                openai.name = f"Достижения_{j}"
                openai.img = f"static/img/{i}.png"
                db_sess.add(openai)
        with open("helpers/text_openai", "w") as flag:
            flag.write("False")
    db_sess.commit()
    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"],\
                                                                           ["История компании"]
    for i in db_session.create_session().query(Openai):
        if 1 <= i.id <= 3:
            achievements_database.append(i.name)
        elif 4 <= i.id <= 6:
            developers_database.append(i.name)
        else:
            company_history_database.append(i.name)
    return render_template("openai.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database)


@app.route("/google")
def google_title():
    with open("helpers/text_google", "r") as flag:
        flag = flag.read()
    db_sess = db_session.create_session()
    print(str(os.path.isfile("db/template_text_google.db")))
    if str(os.path.isfile("db/template_text_google.db")) == flag:
        for j in range(3):
            for i in range(3):
                google = Google()
                google.name = f"Достижения_{j}"
                google.img = f"static/img/{i}.png"
                db_sess.add(google)
        with open("helpers/text_google", "w") as flag:
            flag.write("False")
    db_sess.commit()
    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"],\
                                                                           ["История компании"]
    for i in db_session.create_session().query(Google):
        if 1 <= i.id <= 3:
            achievements_database.append(i.name)
        elif 4 <= i.id <= 6:
            developers_database.append(i.name)
        else:
            company_history_database.append(i.name)
    return render_template("google.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database)


def main():
    db_name = ["db/template_text_openai.db", "db/template_text_yandex.db", "db/template_text_google.db"]
    for i in range(3):
        db_session.global_init(db_name[i])


if __name__ == "__main__":
    main()
    app.run(host="127.0.0.1", port=8080)
