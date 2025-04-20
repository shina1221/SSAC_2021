"""
#스택

삽입/삭제:O(1)
FILO(first in last out) 선입후출
LIFO(last in first out) 후입선출

"""

s= []
s.append(123)
s.append(456)
s.append(789)
print('size', len(s))
while len(s)>0:
    print(s[-1])
    s.pop(-1)

"""
#큐

FIFO first in first out
LILO last in last out

삽입/삭제:O(1)
연결리스트를 이용해 구현하면 삽입/삭제 O(1)구현 가능

원래 파이썬에 from queue import Queue 모듈존재

#thread-safe
#멀티스레드 환경에서 안정성이 보장되나 deque보다 느림
q=Queue()
q.put(123)
q.put(456)
q.put(789)
while q:
    print(q.get())
"""

#d
from collections import deque #double ended queue
#queue가 할 수 있는 역할을 포함
#단 멀티스레드 환경에서 안정성은 보장하지 않음

q = deque()
q.append(123)
q.append(456)
q.append(369)
q.append(789)
print('size', len(q))
while len(q) > 0:
    print(q.popleft())

dq=deque()
dq.append(123)
dq.appendleft(456) #맨 앞에 추가
print(dq.pop())
print(dq.popleft()) #제일 왼쪽에 있는 것부터 pop

