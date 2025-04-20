#DP 구현 2가지
"""
                      TOP-down                                                Bottom-up 
구현        재귀                                            반복문
저장방식    메모이제이션(memoization)                       타뷸레이션
장점        직관적이라 코드 가독성이 좋다                   시간과 메모리를 좀 더 아낄 수 있다.
단점        재귀함수 호출을 많이 해서 느릴 수 있다.         DP테이블 채워 나가는 순서를 알아야 한다.

"""
#백준 11726. 2xn 타일링
"""
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

#풀이 
#f(x)=f(n-1)xf(n-2)

MOD = 10_007 #파이썬에서 _써도 문제없음 콤마대신 사용가능
dp = [-1]*1001
dp[1]=1
dp[2]=2
n = int(input())
for i in range(3,1001):
    print(dp[i-1] + dp[i-2])
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % MOD)

#메모이제이션 사용
import sys
sys.setrecursionlimit(2000)
n = int(input())
cache = [0]*1001
cache[1]=1
cache[2]=2
def box(n):
    #cache[n] = cache[n-1]+cache[n-2]
    if n == 1:
        return 1
    if n ==2:
        return 2
    cache[n]=box(n-1)+box(n-2)
    return cache[n]%MOD
print(box(n))

#백준 10844 쉬운계단수 
"""
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""
#내 방법
MOD=1_000_000_000
N = int(input())
chk_list=[0]*101
chk_list[10]=1
cnt = 0
def chk(n):
    global cnt
    if len(n)==2:
        if max(int(n[0]), int(n[1]))- min(int(n[0]), int(n[1])) == 1:
            chk_list[int(n[0]+n[1])]=chk_list[int(n[1]+n[0])]=1
            cnt+=1
    else:
        for c in range(1,len(n)-1): 
            if abs(int(n[c-1])-int(n[c]))==1 and abs(int(c[n+1])-int(c[n]))==1:
                cnt+=1
    return cnt

for j in range(N+1):
    if N < 10:
        break
    j=str(j)
    chk(j)

print(cnt%MOD)

#풀이
"""
1~8 :+1,-1
0:+1
9:-1

f(n,d):길이가 n이고 마지막 숫자가 d인 계단수 개수

(f(N,0)+f(N,1)+f(N,2)+...+f(N,9))%MOD
f(n,d) =f(n-1,d-1) + f(n-1,d+1) 
        if d>0    // if d<9
"""
#bottom up 방식
#cache[n][d]:길이가 n, 마지막 숫자가 d인 계단수 개수
MOD = 1_000_000_000
cache = [[0]*10 for _ in range(101)]
for j in range(1, 10):
    cache[1][j]=1

for i in range(2, 101):
    for j in range(10):
        if j>0:
            cache[i][j] += cache[i-1][j-1] 

            cache[i][j] %=MOD

        if j<9:
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %=MOD

ans=0
N=int(input())
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)

"""
정리
동적계획법은 문제를 쪼개서 작은 문제부터 구해가며 원래의 답을 구하는 방식
메모이제이션
점화식 찾고 테이블만 잘 정의하면 풀리는 문제들이 많음

"""