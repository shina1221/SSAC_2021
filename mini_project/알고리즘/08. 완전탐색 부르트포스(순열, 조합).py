#완전탐색 

"""
문제 N개의 수를 입력받아서 두 수를 뽑아 합이 가장 클 때는
시간제한 1초, 입력:2=<N=<1,000,000
가능할까?
N=<1,000,000
N Combination 2 = (10^6*(10^6 -1))/2 => 10^12 이므로 불가

=>정렬 알고리즘 사용 => 정렬은 O(NlogN)
"""

"""
#순열
#삼성에서 next_permutation 활용한 문제가 많이 나옴
"""
#python
from itertools import permutations
v= [0,1,2,3]
for i in permutations(v,4):
    print(i)

"""
#조합
"""
from itertools import combinations
v = [0,1,2,3]
for i in combinations(v, 2):
    print(i)

