1) 기본 환경 구축은 virualenv로 -> pipenv가 파이썬 권장이나 버그가 좀 있어서 venv로 합니다
- python3 버젼대로 진행합니다. 다만 파이썬 3.7은 불안정 하니, 3.5 또는 3.6 정도가 적당
$ python --version
$ python -m venv venv  맥 일경우 $ python3 -m venv venv
# requirements.txt 로 설치 -> 있으면

2) chapter_1.py : flask 로 기본 내장 서버 띄우기
2.1) flask 설치 필요 
$ pip install flask

2.2) app.run() 기본 코드 실행

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO WORLD'

if __name__=='__main__':
    app.run()
    
2.3) 화면 설명해야함 : 프론트 화면 / 서버 화면

3) routing 개념 설명