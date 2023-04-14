import sqlalchemy
from .db_session import SqlAlchemyBase


class HomePage(SqlAlchemyBase):
    __tablename__ = 'home_page'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)


class Google(SqlAlchemyBase):
    __tablename__ = 'google_page'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    color = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    alignment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    key_appointments = sqlalchemy.Column(sqlalchemy.Integer)


class Yandex(SqlAlchemyBase):
    __tablename__ = 'yandex_page'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    color = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    alignment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    key_appointments = sqlalchemy.Column(sqlalchemy.Integer)


class OpenAI(SqlAlchemyBase):
    __tablename__ = 'openai_page'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    color = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    alignment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    key_appointments = sqlalchemy.Column(sqlalchemy.Integer)