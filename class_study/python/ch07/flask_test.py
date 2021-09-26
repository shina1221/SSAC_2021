
#Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h1>Hello World!<h1>"
    
#맨 처음 
"""
Error: Could not locate Flask application. You did not provide the FLASK_APP environment variable.
다음의 에러가 뜨면  
명령 프롬프트에서 파이썬 스크립트가 있는 디렉토리로 이동한 다음
Set FLASK_APP = flask_basic.py
flask set 
하고 
커맨드 창에 뜬 주소링크 브라우저에 찍으면 됨

ctrl+c하면 중단임
다시했을 때 localhost:5000/flask_basic으로 들어가주면 됨
"""

@app.route("/")

def hello():
    return "<h2>이 사이트에 온것을 환영해!<h2>"


##함수 데코레이터
def test(f):
    def wrapper():
        print('데코레이터 예시')
        f()
        print('--------절취선--------')
    return wrapper

def hello():
    print('hello')

f1 = test(hello)
f1()

###########
@test  #데코레이터
def playdata():
    print('\플레이데이터에 잘 오셨습니다/')

playdata()


########
@test
def doit():
    print('do it')
    print('go wild')


#<hr/>는 줄긋기


#341p 해보기