"""
이항계수 nCr=nCn-r 
bino(n,0)=1
bino(n,n)=1
bino(n,r)=bino(n-1,r-1)+bino(n-1,r) #삼각수 참조
"""
#백준 11051번 이항계수 2
"""
문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 1,000, 0 ≤ \(K\) ≤ \(N\))

출력
 
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.
"""
import sys

MOD=10007 
#기본 재귀 depth가 1000이므로 재귀함수 횟수제한 풀기
sys.setrecursionlimit(10**7)

cache=[]
N,K = map(int, input().split())

def bino(n,k):
    if k==0 or n == k:
        return 1

    bino(n-1, k-1)+bino(n-1,k)

print(bino(N,K))

#메모이제이션 사용
import sys

MOD=10007 
#기본 재귀 depth가 1000이므로 재귀함수 횟수제한 풀기
sys.setrecursionlimit(10**7)
cache=[[0]*1001 for _ in range(1001)]
def bino(n,k):
    if cache[n][k]:
        return cache[n][k]
    if k==0 or n==k:
        cache[n][k]=1
    else:
        cache[n][k] = bino(n-1,k-1) + bino(n-1,k)
        cache[n][k] %= MOD
    return cache[n][k]

print(bino(N,K))

#bottom up 방식
import sys
sys.setrecursionlimit(10**7)
MOD=10007 
cache=[[0]*1001 for _ in range(1001)]
N,K = map(int, input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1,i):
       cache[i][j] =  cache[i-1][j-1] + cache[i-1][j]
       cache[i][j] %=MOD

print(cache[N][K])
