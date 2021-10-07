"""
#문제 : https://www.acmicpc.net/problem/10872

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.

입출력 예
10         3628800

0          1
"""
"""
10! = 10 x 9!     0! = 1
      9 x 8!
      8 x 7!
      7 x 6!
      6 x 5!
      5 x 4!
      4 x 3!
      3 x 2!
      2 x 1!  
"""
#맨 마지막에 반드시 print 해줘야 함 print 안써서 계속 틀림
#성공
from sys import stdin

def factorial(N):
    if N  <= 1:  #팩토리얼 0이나 1의 값은 1
        answer=1
    else:        
        answer=N * factorial(N-1)
    return answer

N = int(stdin.readline().strip())
factorial(N)

###이하는 시행착오################################################3
from sys import stdin

answer =0
n=N = int(stdin.readline().strip())
def factorial(n, answer):
    if n <= 1:  #팩토리얼 1의 값은 1
        answer=1
    else:            
        answer=n * factorial(n-1, answer)
        #print(answer)
    return answer

factorial(n, answer)

#
from sys import stdin

answer =0
N = int(stdin.readline().strip())
def factorial(n, answer):
    if N == 1 or N == 0:  #팩토리얼 0이나 1의 값은 1
        answer=1
    else:            
        answer=N * factorial(N-1, answer)
    return answer

factorial(N, answer)

#
from sys import stdin

answer=1
def factorial(N, answer):
    if N == 1 or N == 0:  #팩토리얼 0이나 1의 값은 1
        answer=1
    else:        
        answer=N * factorial(N-1, answer)
    return answer

N = int(stdin.readline().strip())
factorial(N, answer)
