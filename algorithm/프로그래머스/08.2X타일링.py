#https://school.programmers.co.kr/learn/courses/30/lessons/12900

#풀이
#https://school.programmers.co.kr/questions/20498
import sys
sys.setrecursionlimit(30000)

def dp(length, history):
    if length in history:
        return history[length]

    history[length] = (dp(length-2, history) + dp(length-1, history)) % 1000000007
    return history[length]

def solution(n):
    history = {-1 : 0, -2 : 0, 0 : 0, 1: 1, 2: 2}

    return dp(n, history)

#개인 시도
#실패, 시간초과
def solution(n):
    answer=0
    if n < 3:
        answer=n
        return answer
    tot=[1,2]
    for nn in range(2,n):
        tot.append(tot[nn-2]+tot[nn-1])
    answer=tot[-1]%1000000007
    return answer


#2차 성공
def solution(n):
    answer=0
    if n < 3:
        answer=n
        return answer
    n1=1
    n2=2
    for nn in range(3,n+1):
        answer=n1+n2
        n1=n2
        n2=answer
    return answer%1000000007


        

#
