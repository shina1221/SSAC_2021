#모듈
def suum(*num):
    return sum(num)

#_변수명 : import할 때 정의되지 않음
#from fibo import *는 _*를 제외하고 모든 모듈을 불러옴

"""


#from test_module import ssum
#import ch07.test_module로 디렉토리 기준으로 작성해도 무방 
#단 해당 디렉토리 내에 인터렉티브 셸이 있어야 함.
#ssum.__name__ 

#from importlib import reload >>>???
#reload(ssum) >>>???

#if __name__ == '__main__': >>>???

#dir() 전역스페이스 확인 
#from fibo import *를 했을 경우 
 #fibo.fib2()는 못함 
 #fib2()로 가능

 #import fibo 하면
 #fibo.fib2() 가능

 #07디렉토리에 있음
 #python fibo.py <arguments>  >>python fibo.py 10 20 30
 
 import sys
 #sys.argv[0] 는 파일이름
 #sys.argv[1:]은 인자들 

 import math
#math.sin(1) 여기서 1은 라디안 1

# 모듈
  : 파이썬 스크립트 파일
  : 확장자 .py
  : 모듈의 정의(변수, 함수, 클래스 등)들은 다른 모듈이나 메인 모듈로 임포트될 수 있음
  * __name__ ⇒ 모듈 이름
    - 모듈이 메인 프로그램으로 실행된다면 __name__ 은 ‘__main__’이라는 문자열을 바인딩함

* import 문
  : 모듈을 임포트

* import 문법
  * import 모듈이름
  * from 모듈 import 정의
    - 정의들은 콤마로 구분하여 나열할 수 있음
  * from 모듈 *
    - 밑줄로 시작하는 정의를 제외한 모든 정의를 임포트 함
    - 권장하지 않음
  * import 모듈이름 as 모듈별칭
  * from 모듈이름 import 정의 as 정의별칭
    - 별칭을 사용하면 이후부터는 별칭으로만 접근해야함

* import 이후에 나열된 이름 혹은 as 이후의 별칭으로 시작하는 이름으로 정의에 접근해야 함

"""
#with raplacement - 복원 추출
#without replacement- 비복원 추출

ㅣ1 = [1,2,3,3,4,5]
from io import TextIOBase
from posix import listdir
import random.shuffle(l1)
print(l1)


import os
os.getcwd()

#os.system('type basic.txt')
#os.systme('notepad abc.py')

#from datetime import datetime
#from 모듈이름 import 모듈의 클래스

#*'년월일시분초' >>언패킹
import datetime
now = datetime.datetime.now()
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*'년월일시분초'))

'{}-{}-{}-{}-{}-{}'.format(*['년도', *'월일시분' '초초')  #???안됨

#################################
from urllib import request

target = request.urlopen('https://google.com')
output = target.read()

print(output)

#살펴보지 않았던 모듈들
"""
re 
functools
pickle- 파이썬 객체를 직렬화(serialize)
d={'name':'hong', : '가가', 'family':{'father': 'hong_f', 'dog' : '길동'}} 

"""
import os
os.listdir()
_ # >> 출력하면 맨 마지막에 출력했던 값이 나옴


import os
output = os.listdir(".")
print("os.listdir():", output)
print()

print('# 폴더와 파일 구분하기')
for path in output:
    if os.path.isdir(path):
        print('폴더:', path)
    else:
        print("파일:",path)

#import os

def read_folder(path):
#330p 못 풀음

