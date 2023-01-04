#https://school.programmers.co.kr/learn/courses/30/lessons/12909
#올바른 괄호
#1차 실패(효율성 통과 못함)
def solution(s):
    while True:
        if '()' not in s:
            if len(s)==0:
                return True
            else:
                return False
        s=s.replace('()','')
    

#https://school.programmers.co.kr/questions/35827 참조
"""
deque mutated during iteration. 오류
deque가 반복문을 돌릴 때 deque의 내용이 변질되거나 사이즈가 변경될 때 뜨는 오류

list를 pop()하면서 for문을 돌려선 안되었기에 while True로 처리해야 했음
이외에도 list while문으로 처리했을 시 시간이 오래걸리기 때문에 queue로 처리해야 했음.
"""
from collections import deque
def solution(s):
    chk=0
    answer=True
    q=deque(s)
    while(q):
        now=q.popleft()
        if now=='(':
            chk+=1
        else:
            chk-=1
            if chk<0:
                answer=False
                break
    if chk>0:
        answer=False
    return answer

"""
for문을 써도 s가 변화가 없었으면 괜찮았고
deque를 안써도 되었음.
"""
#다른 사람의 풀이
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        #ternary operator(삼항 연산자) 여기선 두번씀
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))