# example/test/test_article.py

from .conftest import *

class TestArticle:

    def test_post_article(self, flask_client):
        API = '/article/'
        data = {
            'SUBJECT' : 'I love python',
            'WRITER' : 'Jake',
            'CONTENT':'I love python, flask, pytest..'
        }
        res = flask_client.post(API, data = json.dumps(data), headers=JSON_HEADER)
        assert res.status_code == 200
    
    def test_post_article_with_login(self, flask_client_login):
        res = flask_client_login.post('/article/')