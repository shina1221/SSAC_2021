#파일열기

"""


#path 
# Path(경로)
  * 운영체제의 파일 시스템에서 파일 또는 디렉터리(폴더)을 지칭하는 방법
  * 절대 경로 vs. 상대 경로라
    - 절대 경로: 파일시스템의 꼭대기(윈도: 드라이브명, 유닉스 계열: /(root directory))부터 지정하는 방식
    - 상대 경로: 현재 작업 디렉터리 또는 특정 디렉터리에서 찾아가는 경로

  * 절대 경로는 현재 작업 디렉터리와 상관없이 항상 일정한 경로
    상대 경로는 작업 디렉터리가 변경되면 그에 따라 변경됨

  * 현재 작업 디렉터리: 터미널 환경에서는 항상 특정 디렉터리에 우리가 위치하게 되는데 이 디렉터리를 의미

# 파일 시스템에서 특수한 의미를 갖는 문자(., ..)
  - 윈도, 리눅스 다 동일
  - . : 현재 디렉터리
  - .. : 상위 디렉터리

# 디렉터리와 디렉터리 구분자, 디렉터리와 파일 구분자
  - 윈도: \
  - Unix like system: /

#현재 디렉토리 ..\내가 앞으로 들어갈 디렉토리 

# 프로그램 진입점(Entry point)
  - 프로그램이 시작하는 지점(위치)
                
# 파일 처리
  1) 열기
  2) 읽기, 쓰기, 추가하기
  3) 닫기

# 파일의 읽기 모드

# 파이썬
  - open(): 내장 함수
  - file.close(): 파일 객체의 메서드

#메모리(RAM)
- Cache : 한번 읽은 데이터를 메모리에 저장해 두고 
          같은 데이터를 요청할 때 디스크로부터 읽거나 연산을 통하지 않고 
          메모리에서 바로 읽어서 빠른 속도를 제공하는 메모리 용도 
- Buffer(//영어뜻은 완화하다) : 장치간 데이터 처리속도 차이로 인해 발생하는
                                충돌/속도차를 완화시켜주기 위한 메모리
- pool : 메모리 공간을 미리 준비(확보)해 두고 필요할 때 즉시 제공하여
         빠른 속도를 취할수 있도록 하는 메모리 

# 파일 인코딩
- 텍스트 파일에만 적용
- open()함수에서 설정, 매개변수 encoding
 
"""
file = open('./basic.txt', 'w',  encoding='utf-8')
file.write('오늘은 수요일')
file.close()

#터미널에서 파일 서치
#dir *.txt
"""
# 데이터를 구조화된 정도로 분류
  1) Unstructured Data(비구조적 데이터)
     : 리뷰, 기사, 트윗, 소설, 소셜미디어, 동영상, 음성
  2) Semi-Structured Data(반구조적 데이터)
     : XML, JSON, YAML 등
  3) Structured Data(구조적 데이터)
     : 테이블성 데이터(엑셀 워크시트, DB의 테이블, CSV, TSV)
 
 * Data Cleansing → Data Munging(먼징)

#hangule = list('abcdfer') => 각 글자가 리스트 요소로 반환

with ipen('info.txt', "w") as file:
    for i in range(1000):
        #랜덤한 값으로 변수를 생성
        name = random.choice(hanguls) +rangeom(choi)


#########################
# Shortcut Evaluation
  * and로만 또는 or로만 조건식이 연결되어 있을 때
    - and: 어느 한 조건식이 False면 나머지는 계산할 필요없이 False로 판별
    - or : 어느 한 조건식이 True면 나머지는 계산할 필요없이 True로 판별

ex) a > 0 and b <= 10 and c is abc

ex) a > 0 and b <= 10 and c == takes_long_time_function()


# Generator
  - 우리의 요구에 의해 값을 하나씩 발생해 주는 객체
  - 함수와 비슷한 구조를 가짐
  - def 키워드 사용
  - return 문 대신 yield 문 사용
  - 내부에 이터레이터가 있기 때문에
    -> next() 내장함수로 제너레이터를 실행하고 yield 값을 얻어옴
    -> for 문의 in에 사용될 수 있음

# Generator Expression
  - []대신 ()인것만 제외하면 리스트 내포와 구문적으로 동일
  - 제너레이터 객체를 만듬
  - yield를 사용하지 않음
"""

def test():
    print('함수가 호출되었습니다')
    yield 'test'
print(type(test))

print('A지점 통과')
next(test())

r = next(test())
print(r)

print('B지점 통과')
r= next(test())
next(test())  

def test():
    print('A지점 통과')
    yield 1
    print('B지점 통과')
    yield 2
    print('C지점 통과')

output = test()
#print(type(test)) #<class 'function'>
#print(type(output)) #<class 'generator'>

print('D지점 통과')
a = next(output)
print(a)

print('E지점 통과')
b = next(output)
print(b)

print('F지점 통과')
c = next(output)
print(c)

next(output) #stopiteration오류

######################################
def square(numbers):
    for number in numbers:
        return number * number
data = [1,2,3,4,5]
print(square(data))


def square(numbers):
    for number in numbers:
        yield number * number

g = square(data)
print(next(g)) #1
print(next(g)) #4
print(next(g)) #9
print(next(g)) #16
print(next(g)) #25
print(next(g)) #stopiteration error

g= square(data)
#for n, v in enumerate(g):
for v in g:
    print('{}'.format(v))

ge = (v*v for v in data) #제너레이터 익스프레션
print('ge의 타입: {}'.format(type(ge)))

for v in ge:
    print('{}'.format(v))
next(ge)

#확인문제 
numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))

numbers = list(range(1,10+1))

print("# 홀수만 추출하기")
"""
def get_odd(value):
    return value %2 ==1
print(list(filter(get_odd,numbers)))
"""
print(list(filter(lambda value : value %2 ==1 ,numbers)))
print()

print("#3 이상, 7미만 추출하기")
print(list(filter(lambda value :  3 <= value <7 ,numbers)))
print()

print("#제곱해서 50미만 추출하기")
print(list(filter(lambda value : value**2 <50  ,numbers)))
print()
