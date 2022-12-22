#https://school.programmers.co.kr/learn/courses/30/lessons/77885

import sys
test=list(map(int,sys.stdin.readline().split()))

#비트 연산 bin(10진수)
# int('1101', 2)    # 2진수로 된 문자열 1101을 10진수로 변환    

#두번째
#참조 #https://school.programmers.co.kr/questions/37104
answer=[]
test=[2,4,6,5,3]
for i in test:
    now=bin(i)[2:]
    print(i, 'now_before',now)
    now_l = list(now)
    #짝수일 때
    if i %2 ==0:
        now_l[-1]='1'
    #홀수일 때
    else:
        if len(set(now))==1:
            now_l.insert(0,'1')
            now_l[1]='0'
        else:
            idx=now[::-1].index('0')
            now_l[-(idx+1)]='1'
            now_l[-idx]='0'
    print(i, 'now_after',now_l)
    answer.append(int(''.join(now_l),2))

#실패
answer=[]
for i in test:
    print('i',i)
    now=bin(i)[2:]
    print('now',now)
    now_l = list(now)
    print('now_l',now_l)
    if len(set(now))==1:
        #맨앞에 1추가
        #list(now).insert(0,'1') 이렇게 하면 값 None    
        now_l.insert(0,'1')
        now_l[1]='0'
        print('now_l1',now_l)
    else:
        idx=now[::-1].index('0')
        #오른쪽에서 가장 가까운 0을 1로 변환
        #now[-(idx+1)]=1 이 상태로 값을 변경하려고 하면
        #TypeError: 'str' object does not support item assignment 에러가 뜸
        #이는 문자열이 immutable type으로 튜플과 같이 수정 불가능한 자료구조이기 때문
        now_l[-(idx+1)]='1'
        print('now_l2',now_l) 
    #10진수 변환
    answer.append(int(''.join(now_l),2))
    print('answer',answer)
