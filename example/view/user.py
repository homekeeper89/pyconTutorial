# example/view/user.py
from . import *

@api_user.route('/', methods = ['POST'])
def user_register():
    data = json.loads(request.data)
    mock_database_write(data, USER_FILE)
    return 'SUCCESS', 200

@api_user.route('/<string:usermail>')
def user_login(usermail):
    req_data = request.json

    def finder(condition, iter):
        user_id = condition['EMAIL']
        pwd = condition['PWD']
        if iter.get('EMAIL') == user_id and iter.get('PWD') == pwd:
            return iter

    data = mock_database_read(USER_FILE)
    res = list(filter(lambda dict_obj: finder(req_data, dict_obj), data.values()))
    
    if not res:
        return 'NO USER', 204
    return usermail