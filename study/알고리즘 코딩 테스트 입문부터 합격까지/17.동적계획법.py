"""
Dynamic Programming
문제를 쪼개서 작은 문제의 답을 구하고, 그걸로 더 큰 문제의 답을 구하는걸 반복
분할정복과 비슷한 느낌

#구현 2가지
Top down
구현 :재귀
저장방식:메모이제이션
#메모이제이션 
 - 부분 문제의 답을 한번 구했으면 또 구하지 않도록 (중복연산 방지)
 - cache에 저장해두고 다음부터 갖다씀
 - 필요한 부분 문제들만 구함(lazy evaluation)


Bottm up
구현:반복문
저장방식:타뷸레이션
#타뷸레이션
 - 부분문제들의 답을 미리 다 구해두면 편함(eager evaluation)
 - 테이블을 채워나간다는 의미
"""

#예시
"""
피보나치 수열
f(0)=0
f(1)=1
f(i+2) = f(i+1)+f(i)

                              f(6)
          f(4)                                 f(5)
   f(2)           f(3)               f(3)              f(4)
f(0)  f(1)     f(1)  f(2)        f(1)   f(2)        f(2)    f(3) 
                   f(0) f(1)          f(0) f(1)  f(0) f(1) f(1) f(2) 
                                                              f(0) f(1)   
"""

#백준 2747번. 피보나치 수 
"""
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.
"""
cnt=0
def fi(now):
    global cnt
    cnt+=1
    if now == 1:
        return 1
    if now == 0:
        return 0
    if now>=2:
        return fi(now-1)+fi(now-2)

#풀이
#top down
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n-1) + f(n-2)

print(f(int(input())))

#bottom up(메모이제이션) #훠어얼씬 빠름
cache = [-1]*91 #-1이면 n번째 수는 구한적 없는 수
cache[0] = 0
cache[1] = 1
cnt=0

def f(n):
    global cnt
    cnt+=1
    if cache[n] == -1:
        cache[n] = f(n-1)+f(n-2)
    return cache[n]

#다른 풀이
N = int(input())
cache =  [-1]*91
cache[0] = 0
cache[1] = 1

for i in range(2,N+1):
    cache[i] = cache[i-1]+cache[i-2]

print(cache[N])