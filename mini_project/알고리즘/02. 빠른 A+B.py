n = input().split()
print(n)

a, b = map(int, input().split())
print(a)
print(b)

#빠른 입력
import sys

#주피터에서는 안됨 다른 파이썬 셸을 사용하는 것을 추천
sys.stdin.readline()

for _ in range(10):
    n = int(sys.stdin.readline())
    print(n)

"""
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우.
rstrip()을 추가로 해 주는 것이 좋다.
"""

#예제입력
"""
5
1 1
12 34
5 500
40 60
1000 1000
"""

#예제 출력
"""
2
46
505
100
2000
"""
print(sys.stdin.readline().rstrip())

import sys

for _ in range(int(sys.stdin.readline())):
    print(sum(list(map(int, sys.stdin.readline().rstrip().split()))))

"""
오버플로우
자료형이 담을 수 있는 범위를 초과한 값을 넣을 때 발생하는 문제
python은 고려하지 않아도 됨
"""