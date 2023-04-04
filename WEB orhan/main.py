from data import db_session
from data.template_text import User, Google, Openai, Home_page
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"


@app.route("/home")
def home_title():
    with open("helpers/home_page", "r", encoding="utf-8") as flag:
        full_text = flag.read()
        text_list = full_text.split("\n")
        text, flag = text_list[1::], text_list[0]
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text.db")) == flag:
        for i in range(3):
            home = Home_page()
            home.name = text[i]
            home.img = f"static/img/{i}.png"
            db_sess.add(home)
        db_sess.commit()
        with open("helpers/home_page", "w", encoding="utf-8") as flag:
            new_text = full_text.replace("True", "False")
            flag.write(new_text)
    text_database = []
    index_id = db_sess.query(Home_page.id).count() // 3 - 1
    for i in db_sess.query(Home_page):
        if 1 + 3 * index_id <= i.id <= 3 + 3 * index_id:
            text_database.append(i.name.split("#"))
    return render_template("main_page.html", text_database=text_database, name="Scrovex")


@app.route("/home/yandex")
def yandex_title():
    with open("helpers/text_yandex", "r", encoding="utf-8") as flag:
        full_text = flag.read()
        text_list = full_text.split("\n")
        text, flag = text_list[1::], text_list[0]
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text.db")) == flag:
        for j in range(3):
            for i in range(3):
                yandex = User()
                if j == 1:
                    i += 3
                elif j == 2:
                    i += 6
                yandex.name = text[i]
                yandex.img = f"static/img/{i}.png"
                db_sess.add(yandex)
        db_sess.commit()
        with open("helpers/text_yandex", "w", encoding="utf-8") as flag:
            new_text = full_text.replace("True", "False")
            flag.write(new_text)

    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"], \
                                                                           ["История компании"]
    index_id = db_sess.query(User.id).count() // 9 - 1
    for i in db_sess.query(User):
        if 1 + 9 * index_id <= i.id <= 3 + 9 * index_id:
            achievements_database.append(i.name)
        elif 4 + 9 * index_id <= i.id <= 6 + 9 * index_id:
            developers_database.append(i.name)
        elif 7 + 9 * index_id <= i.id <= 9 + 9 * index_id:
            company_history_database.append(i.name)
    return render_template("blocks_of_information.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database, name="Yandex")


@app.route("/home/openai")
def openai_title():
    with open("helpers/text_openai", "r", encoding="utf-8") as flag:
        full_text = flag.read()
        text_list = full_text.split("\n")
        text, flag = text_list[1::], text_list[0]
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text.db")) == flag:
        for j in range(3):
            for i in range(3):
                openai = Openai()
                if j == 1:
                    i += 3
                elif j == 2:
                    i += 6
                openai.name = text[i]
                openai.img = f"static/img/{i}.png"
                db_sess.add(openai)
        db_sess.commit()
        with open("helpers/text_openai", "w", encoding="utf-8") as flag:
            new_text = full_text.replace("True", "False")
            flag.write(new_text)
    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"],\
                                                                           ["История компании"]
    index_id = db_sess.query(Openai.id).count() // 9 - 1
    for i in db_sess.query(Openai):
        if 1 + 9 * index_id <= i.id <= 3 + 9 * index_id:
            achievements_database.append(i.name)
        elif 4 + 9 * index_id <= i.id <= 6 + 9 * index_id:
            developers_database.append(i.name)
        elif 7 + 9 * index_id <= i.id <= 9 + 9 * index_id:
            company_history_database.append(i.name)
    return render_template("blocks_of_information.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database, name="Openai")


@app.route("/home/google")
def google_title():
    with open("helpers/text_google", "r", encoding="utf-8") as flag:
        full_text = flag.read()
        text_list = full_text.split("\n")
        text, flag = text_list[1::], text_list[0]
    db_sess = db_session.create_session()
    if str(os.path.isfile("db/template_text.db")) == flag:
        for j in range(3):
            for i in range(3):
                google = Google()
                if j == 1:
                    i += 3
                elif j == 2:
                    i += 6
                google.name = text[i]
                google.img = f"static/img/{i}.png"
                db_sess.add(google)
        db_sess.commit()
        with open("helpers/text_google", "w", encoding="utf-8") as flag:
            new_text = full_text.replace("True", "False")
            flag.write(new_text)

    achievements_database, developers_database, company_history_database = ["Достижения"], ["Разработчики"],\
                                                                           ["История компании"]
    index_id = db_sess.query(Google.id).count() // 9 - 1
    for i in db_sess.query(Google):
        if 1 + 9 * index_id <= i.id <= 3 + 9 * index_id:
            achievements_database.append(i.name)
        elif 4 + 9 * index_id <= i.id <= 6 + 9 * index_id:
            developers_database.append(i.name)
        elif 7 + 9 * index_id <= i.id <= 9 + 9 * index_id:
            company_history_database.append(i.name)
    return render_template("blocks_of_information.html", developers_database=developers_database,
                           achievements_database=achievements_database,
                           company_history_database=company_history_database, name="Google")


def main():
    db_session.global_init("db/template_text.db")


if __name__ == "__main__":
    main()
    app.run(host="127.0.0.1", port=8080)
