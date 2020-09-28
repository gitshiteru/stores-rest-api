import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

#Resources are external representaiton
#where client or api use.

class UserRegister(Resource):
    #Avoid name key changes only price
    parser = reqparse.RequestParser()
    #look at JSON payload or form payload to a specific field, ex. "price"
    parser.add_argument(
        'username',
        type = str,
        required=True,
        help= "This field cannot be left blank"
    )
    parser.add_argument(
        'password',
        type = str,
        required=True,
        help= "This field cannot be left blank"
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']) is not None:
            return {"message": "A user with that name already exists."}, 400

        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
