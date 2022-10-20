#외계인의 기타연주

#https://www.acmicpc.net/problem/2841

#풀이
#한번 넣거나 한번빼거나 해서 O(1)
#근데 n개만큼 하니까 O(N)

#stack

import sys

input = sys.stdin.readline
N, P = map(int, input().split())
stk = [[] for _ in range(7)] #줄이 6개(1부터 6까지)
ans=0
for _ in range(N): 
    line, p = map(int, input().split())
    if stk[line] and stk[line][-1] > p:
        stk[line].pop()
        ans +=1 #손가락 움직인 횟수

    if stk[line] and stk[line][-1] == p:
        continue

    stk[line].append(p)
    ans +=1

print(ans)

#예시
"""
5 300000
2 8       >> [8] +1
2 2       >> [2] 8빼고 2넣고 +2
2 300000  >> [2, 300000] 300000넣고 +1
2 8       >> [2, 8] 300000빼고 8넣고 +2  
2 5       >> [2, 5] 8빼고 5넣고 +2

데이터 수가 많아서 제한시간 내에 하려면 stack으로 해야함
"""

#개인 실패
def chk(line_n, fret_n):
    past_fret, past_line = -1, -1
    fret_n = fret_n
    cnt=0   
    for _ in range(line_n):
        now_line, now_fret = map(int, sys.stdin.readline().split()) 
        if cnt==0: #맨처음 입력
            past_fret, past_line = now_fret, now_line
            cnt+=1
            print('cnt+1 맨처음', cnt)
        else: #두번쩨 부터
            cnt+=1 #한번 누른것
            print('cnt+1 입력', cnt)
            print('past', past_line, past_fret)
            if now_line != past_line: #줄바뀜
                past_fret, past_line = now_fret, now_line
                cnt+=1 #떼는 것
                print('손 떼기', cnt)
            else: #줄 그대로 이어짐
                if now_fret<past_fret: # 프렛바뀜
                    cnt+=1 #손 뗌
                    print('줄 그대로인데 프렛 변경+1', cnt)    
                else: #프렛안바뀜
                    print('줄 그대로 누른 상태 더 큰프랫으로 이동', cnt)
                    past_fret, past_line = now_fret, now_line
    print('final', cnt)
    return cnt

import sys
line_n, fret_n =map(int,sys.stdin.readline().split())
chk(line_n,fret_n)
1 5
2 3
2 5
2 7
2 4
1 5
1 3