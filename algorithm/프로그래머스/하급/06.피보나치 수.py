#https://school.programmers.co.kr/learn/courses/30/lessons/12945


#1차 실패>>런타임 에러가 나는 이유로 재귀호출 횟수 제한이 있음 
#따라서 for 문을 사용해 피보나치 수를 구해보자>>동적계획법
def solution(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        answer= solution(n-1)+solution(n-2)    
        return answer%1234567

#2차 완료
def solution(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        fir=0
        sec=1
        thir=0    
        for i in range(1,n):
            thir = fir+sec
            fir=sec
            sec=thir
        return thir%1234567

#다른 사람의 풀이
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a