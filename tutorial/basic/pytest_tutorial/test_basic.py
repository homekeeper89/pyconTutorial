from . import *
# chapter 1 기본 
# pytest 는 기본적으로 test_ 로 시작하는 함수를 모두 찾아내서 그 중에서 실행
# 함수별로 작성해도 되고 class로 작성해도 됨
# pytest -k function 
# pytest -k classBasic
# 모듈로 돌리기 : pytest cp_1_test.py
# 모듈 아래서 특정 함수 돌리기 : pytest test_mod.py::test_func
# 경로로 돌리기 : pytest pytest_tutorial/
# 특정 키워드로 돌리기 : pytest -k 'function', pytest -k function

# 로그 남기기 pytest -k function > test.log
# pytest --junit-xml=report.xml | tee log_for_testers.log

def test_name():
    name = 'jake'
    assert name == 'jake'

def test_age():
    age = 31
    assert age == 28

def test_hobby():
    hobby = 'coding'
    assert hobby == 'python'

def test_jake_hobby():
    hobby = 'python'
    assert hobby == 'python'