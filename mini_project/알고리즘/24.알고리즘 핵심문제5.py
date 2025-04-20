#케빈 베이컨의 6단계 법칙
#https://www.acmicpc.net/problem/1389

#풀이
#BFS 활용 //플로이드 와샬도 사용가능
#양방향 그래프

"""
1-3-4-9
1-7-9
이때는 2

모든 쌍 사이의 최단 거리를 구해야 함.
"""

N, M = map(int, input().split())
#인접리스트 사용
#
adj =[[] for _ in range(N)]
for _ in range(M):
    a,b = map(lambda x: x-1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

#for row in adj:
#    print(row)

kevin = []
ans = (-1, 10000)

from collections import deque
def bfs(start, goal):
    chk = [False]*N
    chk[start]=True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d
        
        nd = d+1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt,nd))


def get_kevin(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)

    return tot


for i in range(N):
    kevin.append(get_kevin(i))

print(f'kevin: {kevin}')
"""
#N은 유저의 수
1 - 2: N
1 - 3: N
1 - 4: N
...
1 - N: N
----
N^2
따라서 최대수(디폴트 수)는 1만보다 커야함
"""
#enumerate 활용
for i, v in enumerate(kevin):
    #케빈 베이컨의 수가 가장 작은 사람을 출력하는데 이가 여러 명일 경우에는 번호가 가장 작은 사람을 출력
    #해당 부분은 아래의 조건식으로 가능
    #0번 2점 3번 2점 >> 3번 2점은 그대로 패스
    if ans[1] > v:
        ans = (i,v)

print(ans[0]+1)






#개인 풀이 실패
import sys 
N, M = map(int,sys.stdin.readline().split())
chk = [[0]*M for _ in range(N)]
for _ in range(N):
    p1, p2=map(int,sys.stdin.readline().split())
    chk[p1-1][p2-1]=1
    chk[p2-1][p1-1]=1
    for i in len(chk):
        if chk[i] == min([sum(i)for i in chk]):
            break
    print(i)


