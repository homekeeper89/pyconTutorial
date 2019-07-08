# example/view/user.py
from . import *

@api_user.route('/', methods = ['GET', 'POST'])
def user_register():
    data = json.loads(request.data)
    return 'HELLO WORLD'