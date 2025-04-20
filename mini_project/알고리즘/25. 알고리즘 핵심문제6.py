#가장 큰 정사각형
#https://www.acmicpc.net/problem/1915
"""
1x1 = 1000x1000
2x2 = 999x999
3x3 = 998 x 998
...
1000 x 1000 = 1 x 1

울프람 알파 서치
sigma i^2, i=1...1000
=333,833,500(최대 정사각형 갯수)
시간제한 2초를 넘어감 


입력으로
0 0 0 1 1 1 0
1 0 1 1 1 1 0
1 1 1 1 1 1 1
1 1 0 1 1 1 1
1 1 1 1 1 1 1 
1 1 1 1 1 1 1    >>이때는 4x4가 최대의 사각형
0 1 1 1 1 1 0

똑같은 크기의 dp 테이블을 만듦

점화식
DP(i,j) = i,j칸을 우하단으로 하는 정사각형 최대 크기

0 0 0 1 1 1 0
1 0 1 1 2 2 0  >>이런식으로 현재자리까지 생각했을 때 만들 수 있는 최대 사각형 한 변의 길이를 채워나감
1 1 1 2 2 3 0 
1
1
0

위의  1 1 1
      1 2 2          2 2
      2 2 3 을 보면  2 3  이렇게 됨
      여기서 반드시 좌 대각 위 에 있는 값중 최소값에 +1을 함
    
      0인칸은 무조건 0이 됨
      또한 좌 대각 위에 0이 하나라도 존재할 경우 1이됨

DP(i,j) = min(DP(i, j-1), DP(i-1, j) DP(i-1, j-1))+1    if arr[i][j]==1


"""
#풀이
n,m =map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

for i in range(1,n):
    if arr[i][0] == '1':
        dp[i][0]=1

    for j in range(1,m):
        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans ** 2)



#개인풀이

import sys

n,m = map(int, sys.stdin.readline().split())

total = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]


def chk():
    for nn in range(1,n-1):
        for mm in range(1,m-1):

