#치킨 배달
#https://www.acmicpc.net/problem/15686



#풀이
 """
 만약 13 C M
 13 C 7 = 1716
 집 : 최대 100군데
 100*7*1716 = 1,201,200 (1초이내 연산 가능)
 """
#완전탐색
from itertools import combinations

N,M = map(int, input().split())
#좌표를 넣기 위한 리스트
houses = []
chickens = []

for i in range(N):
    #index와 value를 같이 받아옴
    #i:행, j:열, v=값
    for j,v in enumerate(map(int, input().split())):
        #print(f'(({i},{j}): {v}', end='     ')
        if v == 1:
            houses.append((i,j))
        if v == 2:
            chickens.append((i,j))

print(f'houses: {houses}')
print(f'chickens: {chickens}')

#정확히 2N-2보다 집 거리는 크지 않음 ##?????
ans = 2*N * len(houses)

#거리 구하기 함수
def get_dist(a,b):
    #a와 b는 모두 튜플형태만 받음
    return abs(a[0]-b[0])+abs(a[1]-b[1])


#M개를 고르는 모든 조합
for combi in combinations(chickens, M):
    tot = 0     #도시의 치킨거리
    for house in houses:
        for chicken in combi:
            tot += min(get_dist(house, chicken) for chicken in combi)
    
    print(f'combi: {combi}', 'tot: {tot}')
    ans = min(ans, tot)

#개인 실패
#셀때는 1부터 시작

import sys
import numpy as np

N,M=map(int,sys.stdin.readline().split())
total=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

one_index_list=[]
two_index_list=[]

for m in range(N):
    for i in range(N):
        print(f'total[{m}][{i}]',total[m][i])
        #가장 가까운 치킨집을 찾는다
        if total[m][i] == 1:
            one_index_list.append([m,i])
        if total[m][i] == 2:
            two_index_list.append([m,i])

result_list={}

for t in two_index_list:
    print(list(map(abs, list(map(min, np.array([t for _ in range(len(one_index_list))]) -np.array(one_index_list))))))
    chk=list(map(sum,list(map(abs, list(map(min, np.array([t for _ in range(len(one_index_list))]) -np.array(one_index_list)))))))

#최대 합을 보이는 값을 삭제
cnt=0

while True:
    if sum(chk[cnt]) == min(map(sum(), chk)):
        chk.pop(chk[cnt])
    cnt+=1
    if M == len(chk)-cnt:
        break




    #list(map(abs,list(map(min, np.array(t for _ in range(len(one_index_list)))))-np.array(one_index_list)))

    #result_list[str(t)]= list(map(abs,list(map(min, np.array(t for _ in range(len(one_index_list)))))-np.array(one_index_list)))




    
