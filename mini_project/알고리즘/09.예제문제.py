#2309 일곱난쟁이
import sys
from itertools import permutations
from itertools import combinations
import heapq

candidates = []

#while now != '\n':
for _ in range(9):
    candidates.append(int(sys.stdin.readline().rstrip()))

for n in combinations(candidates, 7):
    if sum(n) == 100:
        #print(n)
        answer = list(n)
        for n in sorted(answer):
            print(n)
        break

#풀이
from itertools import combinations

heights = [int(input()) for _ in range(9)]
for comb in combinations(heights, 7):
    if sum(comb) == 100:
        for c in sorted(comb):
            print(c)    

#다른 방법
def f():
    heights = [int(input()) for _ in range(9)]
    heights.sort()
    tot = sum(heights)
    for i in range(9):
        for j in range(i+1, 9):
            if tot - heights[i] - heights[j] ==100:
                for k in range(9):
                    if i != k and j != k:
                        print(heights[k]) 
                # 프로그램 종료하는 것
                # exit() 
                return
f()

"""
            heights.remove(heights[j])
            heights.remove(heights[i])
            break
for h in range(heights):
    print(h)
"""

        

