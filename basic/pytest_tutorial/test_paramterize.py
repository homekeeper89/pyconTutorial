from . import *

# 동일한 기능을 다른 input을 넣어야 하는 경우

USER_LIST = {
    'JAKE' : {
        'JOB' : 'FE',
        'FAVORITE':'PYTHON'
    },
    'KIM' : {
        'JOB':'BE',
        'FAVORITE':'PYTHON'
    },
    'LEE' : {
        'JOB':'BE',
        'FAVORITE':'REACT'
    },
    'PARK' : {
        'JOB':'BE',
        'FAVORITE':'VUE'
    }
}

def login_checker(standard):
    """실제론 DB에 접근하는 로그인 로직임"""
    if standard == 'PYTHON':
        return True
    return False

def test_user_login():
    for name, value in USER_LIST.items():
        assert login_checker(value['FAVORITE']), 'Not python user'

@pytest.mark.parametrize("user_type, expected",
        [('PYTHON', True),
        ('java', False),
        ('linux', False)]
)
def test_another_login(user_type, expected):
    assert expected == login_checker(user_type)
    