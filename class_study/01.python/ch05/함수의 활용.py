#함수의 활용

"""
노드
  | 링크
브랜치
  |
리프

# 재귀 함수(Recursive function)
  - 함수가 함수내에서 자기를 호출하는 함수
  - 반드시 재귀를 종료할 수 있는 단계가 필요
  - 복잡한 문제를 간단히 해결할 수 있음
  - 단점: 메모리 과다 사용, 속도 저하

# 메모화(Momoization)  -- cf.) Momorization이 아님.
: 중간계산결과를 저장해놓고 해당 계산을 다시 계산하지 않고 다시 가져다 쓰는 기법

  - (computer science) A technique in which partial results are recorded (forming a memo) and then can be re-used later without having to recompute them.
  - 재귀 함수의 단점 해소 방법
"""
"""
변수 생성과 변수 접근 측면에서의 변수 종류
- 전역변수 (global variable)
 :프로그램 어디에서든 접근 가능
 :프로그램이 종료하면 소멸
- 지역변수 (local variable)
 :코드 블록 내부에 선언/생성된 변수
 :해당 코드 블록 내부에서만 접근 가능
 :해당 코드 블록을 벗어나면 소멸
#파이썬 
    * 전역 변수
        - 메인 프로그램(인터렉티브 셸도 포함) 또는 모듈 어디서든 접근 가능
        - 모듈, 인터랙티브에서 생성한 변수
        - 변수를 생성하는 문장에서 생성되고 프로그램이 종료될 때 소멸
    * 지역 변수
        - 함수에서 생성한 변수
        - 함수의 매개변수
        -코드 블록에서 생성한 변수(if, for, while...)
        -일반적으로 생성하는 문장에서 변수가 생성되고 코드 블록이 끝나면 소멸, 파이썬은 조금 다름
    *자유변수(Free variable)
        - 변수가 생성된 곳과 접근한 곳이 다른 변수
        ex) - for변수는 for문에서 생성되었지만 for문은 물론 for 바깥에서도 접근 가능한 것
            - 메인 프로그램 또는 모듈의 전역변수는 함수 내부에서 접근 가능

#global 문
  - 함수 내부에서 사용하는 자유 변수가 전역 변수임을 선언
  - 전역 변수를 함수 내부에서 변경할 필요가 있을 때 사용
  cf.) nonlocal       

#함수를 활용하여 주석/설명
def get_number_from_user():
return float(input('반지름 입력> "))

def get_circumference(redius):
"""

"""
함수 고급
# first class citizen(일급 객체)
  - 다른 객체들에 일반적으로 적용 가능한 연산을 모두 지원하는 객체
  - 적용 가능한 연산
    : 변수 대입, 함수의 인자로 사용, 수정, 함수의 반환값 등
  - 리터럴, 변수, 객체

# 파이썬에서 함수도 일급 객체이다.

# Closure(클로저)
  - 함수가 종료되어도 자유 변수가 소멸되지 않음

#튜플
-리스트와 비슷하나 요소의 값을 변경할 수 없음
-튜플 만들때 괄호 생략가능 #t1 = 100,200,300,500
-함수가 여러 값을 반환하면 튜플로 묶어서 반환됨(일종의 Packing)
 : 반환값을 하나의 변수로 받을 수도 있고 여러 번수의 값을 받을 수도 있음. 
-요소가 하나인 튜플 생성(값 뒤에 콤마를 붙여야 함)

# 튜플의 요소를 변경할 수 없지만, 튜플의 요소가 변경가능한 리스트, 딕셔너리라면 리스트와 딕셔너리에 저장된 요소는 변경가능함
>>> t1 = (1, 2, ['hello', 100])
>>> t1[2]
['hello', 100]
>>>
>>> t1[2] = 300
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t1[2][0] = 'world'
>>> t1
(1, 2, ['world', 100])


#람다 표현식(이름없는 표현식)
  - 이름 없는 함수 객체를 반환
    → 1회 사용 목적으로 활용
  - 여러번 사용하려면 변수에 바인딩하면 됨

#def 함수명(인자1, 인자2):
    return 표현식

>> lambda 인자1, 인자2 : 표현식

s= lambda x,y: x+y
print(s(10,20))

power = lambda x: x**
under = lambda x: x<3

#확인문제
print('::'.join([str(number) for number in numbers]))

numbers = [1,2,3,4,5,6]
print('::'.join(map(str, numbers)))
print('::'.join(map(lambda x : str(x),numbers)))


# Lazy evaluation <-> Eager evaluation, Greedy evaluation
"""
