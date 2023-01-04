#https://school.programmers.co.kr/learn/courses/30/lessons/12924
#숫자의 표현
def solution(n):    
    plus_n=1
    answer=0
    if n<=2:
        return 1
    for nn in range(1,n):
        if nn%2==0:
            if (n+plus_n)%nn==0:
                answer+=1 
                plus_n+=1
        else:
            if n%nn==0:
                answer+=1
    return answer

#다른 사람의 풀이
#https://school.programmers.co.kr/questions/35202참조

def solution(n):
    answer = 0
    d=1
    while n>0:
        if n%d==0:
            answer+=1
        n-=d
        d+=1

    return answer


#다른 사람의 풀이2
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
