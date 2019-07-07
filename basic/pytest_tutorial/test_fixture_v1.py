from . import *
# chpater2 fixture의 이해
# 아래는 단순한 예시, 공통적으로 테스트 할때 계속해서 불러와야한다고 할 경우 이를 매번 불러 올 것인가?

def login():
    print("Get user info")
    return {'NAME':'JAKE', 'AGE':11}

def logout():
    print("Delete user info")

def test_do_something_with_user_one():
    res = login()
    print(res)
    print("Do something")
    logout()

def test_do_something_with_user_two():
    res = login()
    print(res)
    print("Do something others")
    logout()