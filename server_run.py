# pyconTutorial/server_run.py
# 서버를 실제 런 하는 부분

from app import create_app

app = create_app()

if __name__ =='__main__':
    app.run()