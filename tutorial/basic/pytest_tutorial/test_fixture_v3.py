from . import *
# chpater2 fixture의 이해
# 아래는 단순한 예시, 공통적으로 테스트 할때 계속해서 불러와야한다고 할 경우 이를 매번 불러 올 것인가?

def test_do_something_with_fixture_three(DB):
    print("Test Do something_three")
    res = DB
    print(res)

def test_do_something_with_fixture_four(DB):
    print("Test Do something_four")
    res = DB
    print(res)
