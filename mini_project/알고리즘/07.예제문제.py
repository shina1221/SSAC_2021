import sys
#(()())
for _ in range(int(sys.stdin.readline().rstrip())):
    now = sys.stdin.readline().rstrip()
    stack = []
    for n in now:
        if n == '(':
            stack.append(n)
        else:
            if '(' in stack:
                stack.pop()
            else:
                stack.append(n)
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

# 백준 2164 카드2
from collections import deque
import sys

q = deque(range(1, int(sys.stdin.readline().rstrip())+1))
while len(q)>1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())

#백준 11286. 절댓값 힙
import sys
import heapq as hq

mid=[]
for n in range(int(sys.stdin.readline().rstrip())):
    now = int(sys.stdin.readline())
    if now:
        hq.heappush(mid, (abs(now), now))
    else:
        print('mid',mid)
        print(hq.heappop(mid)[1] if mid else 0)

#1302. 베스트셀러
import sys
books= dict()
for _ in range(int(sys.stdin.readline())):
    book = sys.stdin.readline().rstrip()
    if book not in books:
        books[book]=0
    else:
        books[book]+=1

candidate = []
for name, cnt in books.items():
    if cnt == max(books.values()):
        candidate.append(name)

print(sorted(candidate)[0])

"""
#array,vector 
#stack
#queue
#priority_queue
#map
#set
"""
