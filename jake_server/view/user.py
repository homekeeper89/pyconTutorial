from . import *

@user_api.route('/login')
def user_login():
    return 'heloo world'

@user_api.route('/register', methods=['POST'])
def user_register():
    data = request.json
    res = mock_database_write(data, USER_FILE)
    if not res:
        return 'FAIL', 204
    return {"res" : 'SUCCESS'}, 200