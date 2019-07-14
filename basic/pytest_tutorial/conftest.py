from . import *

@pytest.fixture
def DB():
    print('Connect DB')
    return STANDARD_DB