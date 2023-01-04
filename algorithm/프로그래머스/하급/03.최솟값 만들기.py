#https://school.programmers.co.kr/learn/courses/30/lessons/12941
#최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer=sum([z[0]*z[1] for z in zip(A,B)])
    return answer
