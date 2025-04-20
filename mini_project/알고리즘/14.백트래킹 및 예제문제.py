#백트래킹
"""
기본적으로 모든 경우를 탐색하며 DFS/BFS와 방식유사
백드래킹은 가지치기를 통해 탐색 경우의 수를 줄임(가망성이 없으면 가지 않는다)
"""

#백준 11724번 연결 요소의 개수
"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)                   >>> (N(N-1))/2 = N combination 2
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
"""

import sys

#재귀함수 한도 늘리기
sys.setrecursionlimit(10**6)

N, M = map(int,sys.stdin.readline().split())
#coords = [[0 for _ in range(N)] for _ in range(N)]
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    #u,v = map(lambda x : x-1, map(int, input().split()))
    u,v = map(int,sys.stdin.readline().split())
    adj[u-1][v-1]=adj[v-1][u-1]=1  #무방향이므로 반대방향도 처리 #포인트

#그래프 확인
#for row in adj:
#    row

ans = 0
chk = [False] * N #간선방문확인

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt]=True #미리 체크해서 연산의 낭비를 막을 수 있는 경우가 있음
            dfs(nxt) 

for i in range(N):
    if not chk[i]:
        ans +=1
        chk[i] = True
        dfs(i)

print(ans)

#백준 2178 미로탐색
"""
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

#bfs문제
"""
from collections import deque

#마지막 골인점은 항상 우측 하단임을 명심
dy = (0,1,0,-1) #y는 숫자가 올라갈수록 행렬의 밑으로 이동 #행이동 #y기준 #좌표의 앞부분(y,x)
dx = (1,0,-1,0) #x는 숫자가 올라갈수록 행렬의 우측으로 이동 #열이동
N, M = map(int, sys.stdin.readline().split())
board = [input() for _ in range(N)]

def is_valid_coord(y,x):
    print(0 <= y < N and 0 <= x < M) #bool 형태로 나옴
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True #시작점은 1로 체크하고 시작
    dq = deque()
    dq.append((0, 0, 1)) #앞의 두개는 시작좌표 맨 마지막 몇칸을 자나왔는지, 시작부터 세므로 1
    while dq:
        y, x, d = dq.popleft()
        print('poplefted', y,x,d)
        if y == N-1 and x == M-1: # 항상 도착위치로 이동할 수 있는 경우만 고려하기 위해 
            return d
        nd = d+1 #포인트
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            print('1st','ny:', ny, 'nx', nx, 'nd', nd)
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                print('second', 'ny:', ny, 'nx', nx,'nd', nd)
                dq.append((ny, nx, nd))

bfs()
#정리
"""
그래프는 node 와 edge로 이루어짐
방향성과 순환성이 각각 있거나 없거나 
 - 둘다 없으면 트리

다른 그래프/트리 종류와 알고리즘 존재

그래프 구현
1. 인접행렬
-edge가 많은 그래프일 때 쓰는게 좋음
-edge 탐색이 빠름

인접리스트
-edge가 적은 그래프일 때 쓰는게 좋음
-메모리를 적게씀

DFS, BFS, 백트래킹은 전부 완전탐색 알고리즘
-최악의 경우 모든 노드를 탐색하는건 동일

최단거리를 구할 때는 BFS 사용

DFS는 재귀(or 스택), BFS는 큐로 구현

가지치기를 하면 백트래킹
"""