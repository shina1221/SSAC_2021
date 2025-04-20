#백준 11047.동전 0
"""
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""
import sys
i,j = map(int, sys.stdin.readline().split())
coins = []
cnt=0
for _ in range(i):
    coins.append(int(sys.stdin.readline()))
    
for coin in range(len(coins)-1, -1, -1):
    if coins[coin] > j:
        continue
    cnt+=j//coins[coin]
    j-=(j//coins[coin])* coins[coin]
print(cnt)

#풀이
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K//coin
    K%=coin #나머지
    #print(f'coin: {coin}, K:{K}, ans:{ans}')
print(ans)

#중요###########################################################3
#백준 1449. 수리공 항승
#개인풀이 실패
import sys
#물이새는 곳의 개수, 테이프의 길이 (N,L은 1000보다 작거나 같은 자연수)
N, L = map(int, sys.stdin.readline().split())
#물이 새는 곳의 위치 (1000보다 작거나 같은 자연수)
points = list(map(int, sys.stdin.readline().split()))
points.sort()
cnt = 0

for p in points:
    if p-1 not in points:
        start = p
    if p+1 not in points:
        end = p
        l = end-start +1
        if l%L == 0:
            cnt += l//L
        else:
            cnt += l//L +1

print(cnt)       

#풀이
N, L = map(int, input().split())
coord = [False]*1001 #구멍난 위치만 True로 채울것임
                     #고려해야 할 범위가 1부터 1000이므로 
for i in map(int, input().split()):
    coord[i] = True

ans =0
x = 0 #지금 위치
while x < 1001:
    if coord[x]:
        ans +=1
        x +=L
    else: #구멍이 안난 칸을 만났으면 
        x +=1

