## 해시

# 해시
- 데이터를 다루는 기법 중 하나로 검색과 저장이 아주 유용한 구조로 key와 value로 데이터 저장
- key, 해시함수, 해시테이블로 이루어져있음
- 해시 함수에 의해 각각의 키값이 숫자로 변환 변환된 숫자값들을 해시테이블에서 즉, 하나의 배열에서 인덱스 값으로 사용해 해시테이블에 값 저장
- 해시함수: 임의의 길이를 갖는 메시지를 입력받아 고정된 길이의 해시값을 출력하는 함수
- 데이터의 압축, 암호를 목적으로 미국 나사에서 만들어진 것으로 원리는 불명
- 키값에 작은 변화가 생겨도 완전히 다른 해시값을 반환해 키값을 중복되지 않은 인덱스로 사용가능

# 해시구현방법
- 파이썬에서는 딕셔너리 활용

- 딕셔너리 삽입
: 집합과 배열은 해시함수에 의해 인덱스로 변환 불가하므로 키값으로 사용불가

ex)
hash = dict()
hash[1] ='apple'
hash['banana']=3
hash[(4,5)] = [1,2,3]
hash[10] = dict({1:'a', 2:'b'})
hash[[1,2,3]] ='apple' (불가)
hash[{1,2,3}] = 5 (불가)

- 딕셔너리 수정
: 키값을 기준으로 새로운 값 초기화

ex)
hash[1] = 'melon'
hash['banana']=10

- 딕셔너리 값 추출

ex)
hash.pop(1)         'melon'
hash.pop('banana')  10
hash.pop((4,5))     [1,2,3]
hash.pop(10)        dict({1:'a', 2:'b'})

딕셔너리 삭제

ex)
del hash[1]
del hash['banana]
del hash[(4,5)]
del hash[10]

# 딕셔너리 활용
> 딕셔너리 루프
> 딕셔너리 정렬

- 딕셔너리 루프

ex)
   hash = dict()
 - hash.keys() : key 추출
 - hash.values() : value 추출
 - hash.items() : key와 value 추출

 - 딕셔너리 정렬
 - sorted() : 언제나 list 타입 반환 !
 - 오름차순 정렬

ex)
hash = dict({1:10, 3:12, 5:7, 7:6, 4:5})
sorted(hash.keys(), key = lambda x : x)
 > [1,3,4,5,7]

sorted(hash.values(), key = lambda x : x)
 > [5,6,7,10,12]
          
sorted(hash.items(), key = lambda x : x)
 - 키값을 기준으로 정렬
 > [(1,10), (3,12), (4,5), (5,7), (7,6)] 

 - 내림차순 정렬
 - 마이너스 붙임 (lambda x : -x)

ex)
hash = dict({1:10, 3:12, 5:7, 7:6, 4:5})
sorted(hash.keys(), key = lambda x : -x)
 > [7,5,4,3,1]

sorted(hash.values(), key = lambda x : -x)
 > [12,10,7,6,5]
          
sorted(hash.items(), key = lambda x : -x)
 - 키값을 기준으로 정렬
 > TypeError: bad operand type for unary -: 'tuple'
 why? 튜플의 리스트로 값을 받았기 때문임 즉, x는 튜플인데 튜플에는 -를 붙일 수 없음

 따라서 (lambda x : -x[0]) or (lambda x : -x[1])
 sorted(hash.items(), key = lambda x : -x[0]) #key값 기준
 > [(7, 6), (5, 7), (4, 5), (3, 12), (1, 10)] 
 sorted(hash.items(), key = lambda x : -x[1]) #value값 기준
 > [(3, 12), (1, 10), (5, 7), (7, 6), (4, 5)]

 (x[0], x[1]) >>> key 오름차순, value 오름차순
 (-x[0], x[1]) >>> key 내림차순, value 오름차순
 (x[1], x[0]) >>> value 오름차순, key 오름차순 : 이런식으로 key와 value를 바꿔서도 정렬할 수 있음
       
       