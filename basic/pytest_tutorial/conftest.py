from . import *
# session : 테스트 전체를 아우르는 내용들, ex) 서버 키고 끄기, DB 접속하기, 등
# module : 특정 .py에서만 사용 할 것들 -> login만 테스트 한다고 할 
# function : 특정 기능에서만 사용할 것들
# http://pythontesting.net/framework/pytest/pytest-session-scoped-fixtures/

STANDARD_DB = {
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

@pytest.fixture(scope='session')
def fixture_DB_sesison(request):
    print("Connect DB")
    def DB_OUT():
        print("Disconnet DB")
    request.addfinalizer(DB_OUT)
    return STANDARD_DB

@pytest.fixture(scope='module')
def fixture_user_module(fixture_DB_sesison, request):
    print("Get User who likes Python")
    res = fixture_DB_sesison
    def get_favorite_python(item):
        if item['FAVORITE'] == 'PYTHON':
            return item
    def USER_OUT():
        print("User Module out")
    res = list((filter(get_favorite_python, res.values())))
    request.addfinalizer(USER_OUT)
    return res

@pytest.fixture(scope='function')
def fixture_user_add_hobby(fixture_user_module):
    print('Fixture Function')
    res = fixture_user_module
    return res

@pytest.fixture(scope='function')
def fixture_user_add_sister(fixture_user_module):
    print('Fixture Function')
    res = fixture_user_module
    return res

@pytest.fixture(scope="function", autouse=True)
def check_function(request):
    print('\n === function %s() start ===' % request.function.__name__)
    def fin():
            print('=== function %s() done ===' % request.function.__name__)
    request.addfinalizer(fin)

@pytest.fixture(scope="module", autouse=True)
def check_module(request):
    print('\n >>>> module %s start <<<<' % request.module.__name__)
    def fin():
            print('>>>> module %s done <<<<' % request.module.__name__)
    request.addfinalizer(fin)

@pytest.fixture(scope="session", autouse=True)
def check_session(request):
    print('\n ##### session start #####')
    def fin():
            print('##### session done #####')
    request.addfinalizer(fin)