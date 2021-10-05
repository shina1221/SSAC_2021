## 재귀함수

# 재귀함수
- 메소드 혹은 함수의 내부에서 자기자신의 메소드 혹은 함수를 다시 호출하는 함수

# 예시문제
- data = [3, 5, 8]
성분들의 합으로 표현할 수 있는 숫자의 경우의수는? 부분 집합의 수 2 
2x2x2 = 8가지

0, 3, 5, 8, 3+5, 3+8, 5+8, 3+5+8
            --- 다음과 같이 8이 중복됨
#반복문을 활용한 완전탐색
data = [3,5,8]
result = set()
for i in range(2):
    for j in range(2):
        for k in range(2):
            result.add(data[0] x data[1] x data[2] x k) 

print(result)
>>>>{0, 3, 5, 8, 11, 13, 16}

# 리스트의 수가 많아질 경우
data = [3,5,7,10,12,15,20]
성분의 개수=반복문의 개수

# 재귀함수 원리
def recur(): #호출1
    recur()         def recur(): 
                        recur()  #호출2   ...  def recur(): 
                                                   recur() #호출n

# 재귀함수를 활용한 완전탐색
data=[3,5,8]
def recur(index, value)                        #재귀함수 종료 구문 
    if index == len(data):
        result.add(value)
    else:
        recur(index+1, value+data[index])      #재귀함수 본문
        recur(index+1, value)

##########################################
def recur(index, value)                         
                                                 result=set()
    if index == len(data):
                                                 recur(0,0)
        result.add(value)

    else:
                                                 print(result) 
        recur(index+1, value+data[index])
                                                 {0,3,5,8,11,13,15,17...}
        recur(index+1, value)

# 팩토리얼의 재귀함수 활용
n! = n x(n-1) x 2 x 1

def factorial(n):   
    if n ==1:
        return 1
    else:
    return n x factorial(n-1)

ex) 5!구하기
factorial(5) 120
  > 5 x factorial(4) 5x24
    > 4 x factorial(3) 4x6
      > 3 x factorial(2) 3x2 
        > 2 x factorial(1) 2x1
         
ex) 피보나치 수열의 재귀함수 활용
n=0 n=1 n=2 n=3 n=5 n=6 n=7
  1   1   2   3   5   8  13

def fibonacci(n):
    if n ==0 or n ==1:
        return 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 재귀함수의 깊이
재귀함수가 계속해서 호출될 경우 1000번째를 넘어가는 재귀함수를 호출할 경우 
파이썬에서는 기본적으로 최대깊이가 1000이므로 오류를 나타냄

따라서 다음과 같은 방법으로 재귀함수 호출 횟수를 늘릴 수 있음
import sys
sys.setrecursionlimit(100000)
