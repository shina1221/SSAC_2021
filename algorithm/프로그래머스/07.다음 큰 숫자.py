#https://school.programmers.co.kr/learn/courses/30/lessons/12911
#bin #2진수 
#int('0b???',2)#10진수
#내풀이
def solution(n):
    now_bn = bin(n)[2:]
    a=now_bn.count('1')    
    while True:
        n+=1
        chk_bn = bin(n)[2:]
        b = chk_bn.count('1')    
        if a==b:
            return n

#다른 사람 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n