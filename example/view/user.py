# example/view/user.py
from . import *

@api_user.route('/', methods = ['POST'])
def user_register():
    data = json.loads(request.data)
    mock_database_write(data, USER_FILE)
    return 'SUCCESS', 200