import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'yandex_template'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Openai(SqlAlchemyBase):
    __tablename__ = 'openai_template'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Google(SqlAlchemyBase):
    __tablename__ = 'google_template'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)


class Home_page(SqlAlchemyBase):
    __tablename__ = 'home_template'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
