
10. 연결리스트 / 트리구조

연결리스트는 배열 기반의 리스트(선형 리스트) 와 비슷한 기능을 가진 자료구조 이지만, 선형 리스트와 다르게 노드의 동적 할당과 포인터를 기반으로 구현되기에 메모리 크기에 유연하게 대처가 가능합니다.

트리구조는 트리는 부모-자식 관계로 정의하고, 부모에서 자식으로 간선이 이어져 있는 유향 그래프입니다.

부모 노드 밑에 여러 자식 노드가 연결되고, 자식 노드 각각에 다시 자식 노드가 연결되는 재귀적 형태의 자료구조입니다.



"JEROEN"	56
"JAN"	23

name = "JAN"
name = "JEROEN"


answer = 0
for i in range(len(name)-1):
  now_i = name[i]
  if now_i - name[i+1]
     





answer = 0

now_i = name[0]
if ord('a')-7-ord(now_i) >= ord(now_i)-ord('A'):
    answer+=ord(now_i)-ord('A')
else:
#elif ord('a')-7-ord(now_i) < ord(now_i)-ord('A'):
    answer+=ord('a')-7-ord(now_i)

  
for i in range(1,len(name)):
  print(answer)
  global now_i 
  #기준값 조회
  if min(abs(ord(now_i)-ord(name[i-1]), abs(ord('A')-ord(name[i-1])), abs(ord('Z')-ord(name[i-1]))) == abs(ord(now_i)-ord(name[i-1]):# 기준값은 현재값
    answer+=abs(ord(now_i)-ord(name[i-1])   
    continue
  elif min(abs(ord(now_i)-ord(name[i-1]), abs(ord('A')-ord(name[i-1])), abs(ord('Z')-ord(name[i-1]))) == abs(ord('A')-ord(name[i-1]))) #기준값은 A
    answer=abs(ord('A')-ord(name[i-1]))+1
    continue
  elif min(abs(ord(now_i)-ord(name[i-1]), abs(ord('A')-ord(name[i-1])), abs(ord('Z')-ord(name[i-1]))) == abs(ord('Z')-ord(name[i-1]))) #기준값은 Z
    answer+=abs(ord('Z')-ord(name[i-1]))+1     
    continue

answer
#####
answer = 0

now_i = name[0]
if ord('a')-7-ord(now_i) >= ord(now_i)-ord('A'):
    answer+=ord(now_i)-ord('A')
else:
#elif ord('a')-7-ord(now_i) < ord(now_i)-ord('A'):
    answer+=ord('a')-7-ord(now_i)

for i in range(1,len(name)):
  global now_i 
  now_i = name[i]
  print(answer)
  #기준값 조회
  if min(abs(ord(now_i)-ord(name[i-1])), abs(ord('A')-ord(now_i)), abs(ord('Z')-ord(now_i))) == abs(ord(now_i)-ord(name[i-1])):
    answer+=abs(ord(now_i)-ord(name[i-1])   
  #기준값은 A
  if min(abs(ord(now_i)-ord(name[i-1])), abs(ord('A')-ord(now_i)), abs(ord('Z')-ord(now_i))) == abs(ord('A')-ord(now_i)):
  
    answer+=1
    answer+=abs(ord('A')-ord(now_i))
  #기준값은 Z
  if min(abs(ord(now_i)-ord(name[i-1])), abs(ord('A')-ord(now_i)), abs(ord('Z')-ord(now_i))) == abs(ord('Z')-ord(now_i)):
    answer+=2
    answer+=abs(ord('Z')-ord(now_i))     


now_i = name[0]
for i in range(1,len(name)):
  global now_i 
  print(min(abs(ord(now_i)-ord(name[i-1])), abs(ord('A')-ord(name[i])), abs(ord('Z')-ord(name[i]))))



















  elif abs(ord(now_i)-ord(name[i+1])) # 기준값은 현재값
    +0   
  < abs(ord('A')-ord(name[i+1])) #기준값은 A
    +1
    abs(ord('Z')-ord(name[i+1])) #기준값은 Z
    +2     


