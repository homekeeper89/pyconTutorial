# example/view/article.py
from . import *

@api_article.route('/', methods=['POST'])
def post_article():
    data = request.json
    res = session_checker(session)
    if res:
        res = mock_database_write(data, ARTICLE_FILE)
        if res:
            return 'POST SUCCESS'
    return 'POST FAIL', 204