# 추상(Abstraction)
"""
  - 사전적 의미
    : 여러 가지 사물이나 개념에서 공통되는 특성이나 속성 따위를 추출하여 파악하는 작용.

     - 객체 (Object, 개체)
         : 여러 가지 사물이나 개념


1) None :
2) NotImplemented : 메소드가 명확하지 않음
3) Ellipsis : 타입과 값이 한개
4) numbers.Number(numbsers라는 모듈의 numbers라는 클래스)
    - numbers.Integral: int, bool
    - numbers.Real: float
    - numbers.Complex: complex(복소수 타입)
5) Sequences
    :  finite ordered sets indexed by non-negative numbers(0부터 시작, 순서있음)
    - Immutable Sequences: String, Tuple, Bytes
        :요소를 변경할 수 없음
    - Mutable sequences: Lists, Byte Arrarys
6) Set types
   : unordered, finite sets of unique, immutable objects
   > 정수로 인덱싱 될 수 없음, 중복불허
   - Sets: mutable sets
   - Frozen sets: immutable sets
7) Mappings
   : finite sets of objects indexed by arbitrary index sets
   - Dictonaries
8) Callable types
   - User-defined functions: def 키워드, 반환시 return 문
   - Instance methods: 클래스 정의 내에서 def 키워드, 반환시 return 문
   - Generator functions: def 키워드, 반환시 yield 문 ← next() 내장 함수 사용
   - Coroutine functions:
   - Built-in functions:  sum(), len()
   - Built-in methods:  list.append(), dict.get()
   - Classes:
   - Class Instances: special method __call__()을 미리 정의해 두어야 함   
     >>>객체를 부를 수 있는데 이때 call 정의되어 있어야 함.
"""

"""
# 함수란?
  - function: 기능 → 행위 → action, behavior
  - 함수: 함(상자 함) → B/B(블랙박스), 함수의 입출력에 관심
  - (관련 있는) 코드 블록에 이름 붙인 것
  - parameters(함수의 지역변수) vs. arguments(사용자입장 변수)
  - 함수 헤더(Function signature: 리턴타입, 함수이름, 함수인자)와 함수 바디로 구성

# 파이썬에서 함수 정의
  - def 키워드 사용
  - 함수 헤더에 반환 타입(X)

# 함수를 사용하는 이유
  - 코드 중복 제거
  - 프로그램을 기능별로 구분 → 모듈화

# 파이썬의 arguments 또는 parameters
  1) 위치 인자/매개변수(positional ~~~): 인자/매개변수의 위치로 값 지정 (순서가 중요)
  2) 키워드 인자/매개변수(keyword ~~~): 인자/매개변수의 이름으로 값 지정
(순서는 중요하지 않음)

# 가변 매개변수
  : 매개변수 이름 앞에 *를 붙임 → 위치 매개변수로 인식
  : 매개변수의 개수가 정해지지 않음, 필요한 만큼의 인자를 받음
  - 대표적인 예: print()
  - 제약 : 1) 일반 매개변수 선언이 끝난 후에 가변 매개변수 정의
           2) 가변 매개변수는 1개만 가능
  - 함수 내에서 퓨틀 객체:
  - 함수 호출 시 가변 매개변수를 키워드 지정 방식으로 사용할 수 없음

  
# 기본 매개변수(Default parameters)
  : 인자가 생략될 때 해당 매개변수의 초깃값으로 적용
  - 키워드 인자로 호출될 때 유용
  - 기본 매개변수는 일반 매개변수 이후에 정의

# 함수 호출 시 인자 지정 방식
  1) 위치 지정 방식 : 
  - 매개변수의 식별자를 이용하지 않음
  - 인자의 순서가 중요
  2) 키워드 지정 방식
  - 매개변수의 식별자를 이용
  - 인자의 순서는 중요하지 않음
  3) 위치, 키워드 혼용 방식
    - 위치 인자를 키워드 인자보다 먼저 기술
  4) 기본 매개변수와 위치 지정 방식
  5) 기본 매개변수와 키워드 지정 방식
  6) 기본 매개변수와 위치 및 키워드 지정 방식 혼용

# 가변 키워드 인자
  - cf.) 가변 매개변수를 가변 인자라고도 일컬음

"""

def print_3_times():
    print('안녕하세요\n'*3)

def print_3_times():
    for _ in range(3):
        print('안녕하세요')

#for _,v in dict.items()일 경우 값만 받아쓰겠다는 뜻

def print_2_times():
    for _ in range(2):
        print('안녕하세요')

def print_times(n, msg):
    for _ in range(n):
        print(msg)

#가변 매개변수
def print_n_times(*mag, n):
    print(msg)
#print_n_times('hello',2) >>>이렇게 하면 *mag가 모든 파라미터를 받아서 에러뜸

def print_n_times(n, *msgs):
    print('msg : {}'.format(msgs))
    print('type of msg: {}'.format(type(msgs)))

    for _ in range(n):
        for msg in msgs:
            print(msg)
        print('-'*20)

    for _ in range(n):
        print('\n'.join(msgs))
        print('-'*20)

print_n_times(2,'안녕', 'muyaho', 'Guten Tag')


def print_all(name, age, score='A+', hobby=[]):
    print('name: {}\tage: {}\tscore: {}\thobby: {}'.format(
        name, age, score, hobby
    ))

#위치 지정 방식
print_all('홍길동', 22, 'A+', ['의적','호부호형'])
#이름 지정 방식
print_all(name='홍길동', hobby=['의적', '호부호형'], age=22 score='A+')

#기본 매개변수와 위치 지정
print_all('홍길동', 22)
print_all('홍길동', 22, hobby=['의적', '호부호형'])
print_all('홍길동', 22, 'A+', ['의적', '호부호형'])

#기본 매개변수와 키워드 지정
print_all(age=22, name='홍길동')
print_all(score='C', name='홍길동', age=22)

print_all(score='F', age=22, name='홍길동') 
#>>>위치지정 방식이 먼저와야 함
print_all(age=22, score='F', name='홍길동') 

#print_n_times)=(안녕하세요1', 'hello2','n=3, '안녕하세요', 'hello') 
#>>중간에 키워드 매개변수가 들어가는 순간 뒤에있는 안녕하세요와 hello또한 키워드 매개변수로 들어간다고 인식해서 에러뜸

def print_n_times(title, n=2, *msgs):
#def print_n_times(title, *msgs, n=2):
#정의할 시 디폴트 파라미터를 뒤로 뻄
    print('msgs : {}'.format(msgs))
    print('type of msgs: {}'.format(type(msgs)))

    print('# {}'.format(title))
    
    for _ in range(n):
        print('\n'.join(msgs))
        print('-'*20)

#위치지정 파라미터부터 작성
print_n_times('예제', n=3,'안녕', 'muyaho', 'Guten Tag', '헬로', '헬로우')

#기본매개변수 이외의 것들을 **kwargs(키워드 인자)로 받음##############################3
def print_all(title, n=2, **kwargs):
    print('kwargs = {}'.format(kwargs))
    print('type of kwargs = {}'.format(type(kwargs)))

print_all('예제', 3, name = '홍길동', age=22, hobby = ['의적', '호부호형'])

"""
가변 키워드 인자
  - cf.) 가변 매개변수를 가변 인자라고도 일컬음
         가변 인자: 위치 매개변수
       - 가변 키워드 인자: 키워드 매개변수
  - 제약 : 1) 일반 매개변수와 가변 매개변수 선언이 끝난 후에 가변 매개변수 정의
           2) 가변 매개변수는 1개만 가능         
  - 매개변수 이름 앞에 ** 붙임
  - 함수 내부에서 Dictionary로 처리


# 가변 키워드 인자 활용법
  - wrapper 함수
  - B함수의 인자를 우리가 만든 함수에서 파라미터로 받은 후 해당 파라미터를
  다른 함수를 호출할 때 사용


# Packing vs. Unpacking
  * Packing
   : 인자로 받은 여러 개의 값을 하나의 매개변수로 받을 수 있게 하는 매커니즘
     - Positional argument packing: *args → 튜플로 받음
     - Keyword argument packing: **kwargs → 딕셔너리로 받음

  * Unpacking
   : 하나의 변수에 담긴 여러 개의 값을 여러 인자로 풀어주는 매커니즘
     - Positional argument unpacking: 함수 호출 시 인자(튜플,  앞에 *
     - Keyword argument unpacking: 함수 호출 시 인자(딕셔너리) 앞에 **
   

"""
#title이외에 넣을 매개변수들이 많을경우 **kwargs로 퉁쳐서 넣을 수 있음
def print_v2(title, **kwargs):
    print(title, **kwargs)
print_v2('안녕하세요', end='', sep='\t')


"""

# Packing vs. Unpacking
  * Packing
   : 인자로 받은 여러 개의 값을 하나의 매개변수로 받을 수 있게 하는 매커니즘
     - Positional argument packing: *args → 튜플로 받음
     - Keyword argument packing: **kwargs → 딕셔너리로 받음

  * Unpacking
   : 하나의 변수에 담긴 여러 개의 값을 여러 인자로 풀어주는 매커니즘
"""
#위치인자
def my_func(*args):
    print(args)
    for arg in args:
        print(arg)

my_func(10, 'a', 'hello', [1,2,3], range(100))
my_func('abc', 20)

#키워드인자
def my_func(**kwargs):
    print(kwargs)
    for arg in kwargs:
        print(arg)

#키워드인자 error
my_func(10, 'a', 'hello', [1,2,3], range(100))
my_func('abc', 20)

#
my_func(name='홍길동', age=22, score='a')
my_func(name='무명씨', hight=175, weight=70, address='서울')



#패킹
def my_func(**kwargs):
    print(kwargs)
    for p_name,p_value in kwargs.items():
        print('parameter name: {}, value: {}'.format(p_name, p_value))

def my_sum(*numbers):
    return sum(numbers)

print(my_sum(1,2,3,4,5))

def print(A, B, *C) #*C는 가변인자 키워드 가변인자는 항상 뒤에 온다. 가변인자는 옵션적임. 


# 위치 가변 인자와 키워드 가변 인자를 함께 사용
#  - 위치 가변인자 먼저

def my_sum(x,y):
    return x+yield
print(my_sum(10,20))

values = (10,20)
print(my_sum(*values))

#언패킹
def my_sum(a,b):
    return sum(a+b)

def my_sum(*args):
    return sum(args)

values = (10,20,30)
print(my_sum(*values))
print(my_sum(*[100,200,100]))


def print_all(name, age, job):
    print(name, age, job)

hong = {'name': '홍', 'job': '의적', '나이': 11}
print(*hong)

#문제2
def mul(*values):
    result=1
    for value in values:
        result*=value
    return result

print(mul(2,3,5))

#언패킹 사용
v=[5,7,9,10]
print(mul(*v))