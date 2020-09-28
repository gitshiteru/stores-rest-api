
# That is going to use our app. The authenticate and the identity functions together,
# to allow for authentication of users. So here's how it's going to work.
# JWT creates a new endpoint that endpoint is /auth. When we call /auth.
# We send it a username and a password, and the JWT extension gives that username and password
#  and sends it over to the authenticate function that takes in a username and a password.
#  We're then going to find the correct user object using the username,
#  and we're going to compare its password to the one that we receive to do the auth endpoint.
#  If they match. We're going to return the user. And then becomes sort of the identity.
#  So what happens next is the auth endpoint returns a JWT token. The JWT token.
#  Now, that JWT token in itself doesn't do anything, but we can send it to the next request we make.
#  So when we send a JWT token. What JWT does is, it calls the identity function.
#  And then it uses the JWT token to get the user ID. And with that,
#  it gives the correct user for that user ID that the JWT token represents.
#  And it can do that. That means that the user was authenticated the JWT token is valid.
#  And all is good. So from flask JWT, we're going to import JWT, and JWT required.
#  And that is a decorator that we are going to call in front of our get method.


import os
from flask import Flask
# JWT: JSON Web Token, encoding data
#Resouce is represent to a schema or a data set that Api returns
from flask_restful import  Api
from flask_jwt import JWT
#custome functions in security.py
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
#tell sqlalchemy where to find data.db file
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
#Use better sqlalchemy modification tracker
#U than flask_sqlalckemy one.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ='mantra'
#'Api' works with 'Resource' and every Resource has to be a class
api = Api(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

jwt = JWT(app, authenticate, identity) # /auth end point created

# http://localhost:5000/item/<name>
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    # Must here to avoid Circuler Import
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
