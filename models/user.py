import sqlite3
from db import db
#models are internal representation; resources are external representaiton
#where client or api use.
class UserModel(db.Model):
    __tablename__ = 'users'
    #better to change id to uid, because id is Python's reserved keyword.
    id = db.Column(db.Integer, primary_key=True) #id is auto-incrementing
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        #self.id = _id  #Object created throgh sqlalchemy assign self_id automatically
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        #first username is the tablename followed by argument - username
        return cls.query.filter_by(username=username).first()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # #Parameters are in the form of tuple, so we must state as (username,)
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row is not None:
        #     #user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
