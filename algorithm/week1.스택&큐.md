## stack & Queue

#스택(Stack)
  : - 차곡차곡 쌓아올린 형태의 자료구조
    - 리스트에서 접근이 한쪽에서만 가능
    - LIFO(Last-In, First_out)원리를 가짐

#관련 연산
  1) push: 스택에 새로운 요소 삽입
  2) peek(엿보다): 스택의 최상단 (리스트의 가장 오른쪽) 출력
  3) pop: 스택의 최상단 (리스트의 가장 오른쪽) 요소를 꺼내서 삭제

#python 스택의 구현
  : 파이썬은 리스트를 스택으로 사용할 수 있게 구현
    
#Python 스택 직접 구현
 1) push 
   : 하나의 배열 뒤에 요소를 추가하는 것 
     -> list.append 함수  
 2) peek
   : 마지막 값 반환
     -> def peek(self): 
            return self[-1]
            #or self[len(self)-1] #마지막 값의 인덱스를 넣음
 3) pop  
   : 내장함수로 존재 
     -> list.pop 함수


#Python 스택 직접 구현 예시
-> #Stack 직접구현

   s=Stack()
   s.push(1)
   s.push(5)
   s.push(10)
   print('my stack is : ', s)  #리스트 확인
   >>> my stack is : [1, 5, 10]

   #pop
   
   print('poped value is : ' s.pop())  #마지막 요소 뽑음
   >>> poped value is : 10
   print('my stack is : ', s)
   >>> my stack is : [1, 5]

   #peek
   print(peeked value is : ', s.peek())
   >>> peeked value is : 5 # 마지막 요소 확인
   print('my stack is : ',s)
   >>> my stack is : [1, 5]

#python List를 스택으로 활용

s=[]
s.push(1)
s.push(5)
s.push(10)
print('my stack is : ', s)  #리스트 확인
>>> my stack is : [1, 5, 10]
print('poped value is : ' s.pop())  #마지막 요소 뽑음
>>> poped value is : 10
print('my stack is:', s)
>>> my stack is : [1, 5]
print(peeked value is : ', s.peek())
>>> peeked value is : 5 # 마지막 요소 확인
print('my stack is :',s)
>>> my stack is : [1, 5]

#스택의 활용 예시
: 1) 웹브라우저에서의 이전페이지, 다음페이지 
     현재페이지 : 네이버  // 이전페이지 : []             (다음으로 넘어감)  // 다음페이지 []
     현재페이지 : 구글    // 이전페이지 : [네이버]       (다음으로 넘어감)  // 다음페이지 []
     현재페이지 : 유튜브  // 이전페이지 : [네이버, 구글] (이전으로 돌아감)  // 다음페이지 []
     현재페이지 : 구글    // 이전페이지 : [네이버]       (이전으로 돌아감)  // 다음페이지 [유튜브]
     현재페이지 : 네이버  // 이전페이지 : []             (이전으로 돌아감)  // 다음페이지 [유튜브, 구글]
  2) 깊이우선 탐색에서도 활용



#큐(Queue)//일이 처리되기를 기다리는 리스트
  : - 먼저들어온 자료가 먼저 나가는 구조(FIFO: First In First-Out)
    - 리스트의 양쪽에서 접근가능한 구조
    - 리스트의 한쪽에서는 삽입연산만, 다른 한쪽에서는 삭제연산만 수행
    - 선착순 방식

#관련 연산
  1) put: 큐에 새로운 요소 삽입
  2) peek(엿보다): 가장 먼저 삽입된 요소 출력  ## stack과 반대되는 부문
  3) get: 가장 먼저 삽입된 요소를 꺼내서 삭제

#python 스택의 구현
  : 직접구현, 이미 구현된 클래스 import, List를 큐로 구현
    
#Python 큐 직접 구현
 1) put  
   : 하나의 배열 뒤에 요소를 추가하는 것 
     -> list.append 함수  
 2) peek
   : 첫번째 값 반환
     -> def peek(self): 
            return self[0] #맨 앞의 값
 3) get
   : 내장함수로 존재 
     -> list.pop 함수

#큐 구현
class Queue(list):
    put = list.append()
    def peek(self):
        return self[0]
    def get(self):
    return self.pop(0)


#Python 큐 직접 구현 예시
-> #Queue 직접구현

  a= Queue()
  q.put(1)
  q.put(5)
  q.put(10)
  print('my queue is : ', q)
  >>>my queue is : [1, 5, 10]
  print('removed value is : ', q.get())
  >>>removed value is : 1
  print('my queue is : ', q)
  >>>my queue is : [5, 10]
  print('peeked value is : ', q.peek()) #출력하기만 할 뿐임
  >>>peeked value is : 5
  print('my queue is : ', q)
  >>>my queue is : [5, 10]

-> 구현된 클래스 import
  from queue import Queue
  a= Queue()
  q.put(1) #값을 넣음
  q.put(5)
  q.put(10)
  print('my queue is : ', q)
  >>>my queue is : [1, 5, 10]
  print('removed value is : ', q.get())
  >>>removed value is : 1
  print('my queue is : ', q)
  >>>my queue is : [5, 10]
  print('peeked value is : ', q.peek()) #출력하기만 할 뿐임
  >>>peeked value is : 5
  print('my queue is : ', q)
  >>>my queue is : [5, 10]

-> 리스트를 큐로 구현
 #본인 구현
 list_queue=[]
 list_queue.append(1) 
 list_queue.append(5) 
 list_queue.append(10)
 #peek 첫번째 요소 확인
 print(list_queue[0]) 
 #get 첫번째 요소 추출
 list_queue.pop(0) 

#강의 ver
  q=[]
  q.append(1)
  q.append(5)
  q.append(10)
  print('my queue is : ', q)
  >>>my queue is : [1, 5, 10]
  print('removed value is : ', q.pop(0))
  >>>removed value is : 1
  print('my queue is : ', q)
  >>>my queue is : [5, 10]
  print('peeked value is : ', q[0]) #출력하기만 할 뿐임
  >>>peeked value is : 5
  print('my queue is : ', q)
  >>>my queue is : [5, 10]

#큐의 활용 예시

: 1) 프린터 인쇄 대기열
     프린터는 출력요청을 받은 순서대로 출력 시행
  2) 너비우선 탐색에서도 활용
      
