# view/user.py
from . import *

@user_api.route('/<string:email>', methods=['POST'])
def user_login(email):
    req_data = request.json
    data = mock_database_read(USER_FILE)
    for key, value in data.items():
        if value['EMAIL'] == email and value['PWD'] == req_data['PWD']:
            return {'EMAIL': value['EMAIL'], 'SERVER_MSG': 'LOGIN_SUCCESS'}
    return 'hello world'

@user_api.route('/register', methods=['POST'])
def user_register():
    data = request.json
    mock_database_write(data, USER_FILE)
    return {'RES' : 'SUCCESS'}