#https://school.programmers.co.kr/learn/courses/30/lessons/12985

#풀이
#https://eda-ai-lab.tistory.com/500
"""
각 번호에 1을 더하는 이유
1 ~ 8의 번호가 있을 때, 단순히 2로 나눈 몫은 0 1 1 2 2 3 3 4 이지만 
1을 더했을 경우 1 1 2 2 3 3 4 4가 되므로 원하고자 하는 결과값을 얻을 수 있음
"""
def solution(n,a,b): 
	answer = 0
	while a != b: 
		answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2
	return answer

#시간초과 실패
import sys
N = int(sys.stdin.readline())
A=4
B=7
#3
def solution(N,A,B):
    answer=0
    A=min(A,B)
    B=max(A,B)
    r_N = range(1,N+1)
    while True:
        answer+=1
        #A와 B는 같이 붙어있어야하고 두명당 한팀씩 올라가므로 더 큰수를 가진쪽은 반드시 인덱스가 짝수이어야하고 작은수를 가진쪽은 인덱스가 홀수여야함
        #예시(8,4,5)
        if r_N.index(B)-r_N.index(A)==1 and r_N.index(A)%2==0 and r_N.index(B)%2==1:
            return answer
        r_N=[r_N[n] if r_N[n] in [A,B] else r_N[n+1] for n in range(0,len(r_N),2)]
    

#다른시도

def solution(N,A,B):
    answer=0
    A=min(A,B)
    B=max(A,B)
    if A % 2 == 1:
        srt_idx=A
    if A % 2 == 0:
        srt_idx=A-1
    if B % 2 == 1:
        end_idx=B+1
    if B % 2 == 0:
        end_idx=B-1
    r_N = range(1,N+1)[srt_idx:end_idx+1]

    while True:
        answer+=1
        idx_b = r_N.index(B)
        idx_a = r_N.index(A)
        if idx_b-idx_a==1 and idx_a%2==0 and idx_b%2==1:
            return answer
        r_N=[r_N[n] if r_N[n] in [A,B] else r_N[n+1] for n in range(0,len(r_N),2)]
        
solution(8,4,5)



A=min(A,B)
B=max(A,B)
str_idx=-1
end_idx=-1


if A % 2 == 1:
    str_idx=A-1

if A % 2 == 0:
    str_idx=A-2

if B % 2 == 1:
    end_idx=B+2

if B % 2 == 0:
    end_idx=B+1

r_N = range(1,N+1)[str_idx:end_idx]



answer=0
A=min(A,B)
B=max(A,B)

if A % 2 == 1:
    srt_idx=A-1
if A % 2 == 0:
    srt_idx=A-2
if B % 2 == 1:
    end_idx=B+1
if B % 2 == 0:
    end_idx=B-1

r_N = range(1,N+1)[srt_idx:end_idx]
chk_idx= [2**i for i in range(21)]
for j in range(len(chk_idx)):
    if len(r_N) < chk_idx[j]:
        find_idx=j
        break

min(abs(2**find_idx-))

import math
if len(r_N)**(1/2): 
    

while True:
    answer+=1
    idx_b = r_N.index(B)
    idx_a = r_N.index(A)
    if idx_b-idx_a==1 and idx_a%2==0 and idx_b%2==1:
        print(answer)
        break
    r_N=[r_N[n] if r_N[n] in [A,B] else r_N[n+1] for n in range(0,len(r_N),2)]
