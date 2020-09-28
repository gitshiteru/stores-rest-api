from werkzeug.security import safe_str_cmp
from models.user import UserModel

#in memorty talbe of our registered users
# users = [
#     User(1, 'toshio', '3778')
# ]
# #Set complihension
# username_mapping = {u.username: u for u in users}
# userid_mapping ={u.id: u for u in users}
#
# users = [
#     {
#         'id': 1,
#         'username': 'toshio',
#         'password': 3778
#     }
# ]
# Purpose of following code is to find user or id quickly by name or id
#name is the key
# username_mapping = {
#     'toshio': {
#         'id': 1,
#         'username': 'toshio',
#         'password': 3778
#     }
# }
# #id is the key
# userid_mapping = {
#     1: {
#         'id': 1,
#         'username': 'toshio',
#         'password': 3778
#     }
# }

# def authenticate(username, password):
#     #if user does not exist, return None
#     user = username_mapping.get(username, None)
#     #if user and user.password == password:
#     #Safe for differnt string encodeing, works for python2 or different systems.
#     if user and safe_str_cmp(user.password, password):
#         return user
#
# #identity is unique to JWT and payload is the content of JWT token
# def identity(payload):
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)
#
def authenticate(username, password):
    #if user does not exist, return None
    user = UserModel.find_by_username(username)
    #if user and user.password == password:
    #Safe for differnt string encodeing, works for python2 or different systems.
    if user and safe_str_cmp(user.password, password):
        return user

#identity is unique to JWT and payload is the content of JWT token
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
