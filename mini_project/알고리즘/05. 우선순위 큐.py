"""
#우선순위 큐(heap)
#삽입/삭제 O(logN) #밑이 log2 인 N

그래프 모양 생각하면 됨
"""
#python
#mini heap #가장 상위에 오는 root 값이 가장 작음
#c++에서는 max heap 제공
#thread safe보장되지 않음 대신 빠름
import heapq
pq = []
heapq.heappush(pq, 6)
heapq.heappush(pq, 12)
heapq.heappush(pq, 7)
heapq.heappush(pq, -5)
heapq.heappush(pq, 10)
print('size', len(pq))
while len(pq) > 0:
    #root 노드 값 확인
    print(pq[0]) #파이썬은 mini heap이므로 최소값이 나옴
    heapq.heappop(pq)

#PriorityQueue
#thread safe가 보장되므로 느림
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(4)
pq.put(1)
pq.put(-5)
while not pq.empty():
    print(pq.get()) #pop