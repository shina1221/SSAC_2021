"""
#map
key, value 사용
삽입/삭제 O(1)
키끼리는 중복 불가

c++에서는 red black tree 구조를 사용
python은 hash 구조 사용 #키값에서 hash 함수를 거치면 hash 테이블 상에서 주소를 알 수 있음
"""
m = {}
m['a'] = 40
m['b'] = 50
m['c'] = 60
m['ㄱ'] = 100
print('size', len(m))
for k in m:
    print(k, m[k])

"""
#집합 set
중복불가
삽입, 삭제  O(1)
"""
s= set()
#add
s.add(456)
s.add(12)
s.add(456)
s.add(789)
#s.remove(12) 특정 값을 삭제
#s.pop() #random 값이 삭제 됨 
#s.clear()하면 set 초기화
print(s)
