#Dictionary
"""
-mapping 자료형 >> (k,v) key, value pair
-key는 유일해야 함. 같은 키로 값을 추가하면 해당 키 값이 대체됨
-key immutable 자료형만 가능
:숫자형, 문자열, 불, 튜플 
mappig >>사상

key > value
'가' > '아버지가방에들어가신다'

#빈 딕셔너리 생성
1. d1 = {}
2. d2 = dict();


"""

d1 = {}
d1 = {
    1:"hello",
    '다이아몬드홀':50,
    'a'=120}
#만약 1:'wordl라고 마지막에 지정하면 키 1에 대한 값은 world로 수정됨>>키는 유일해야 함
d1
#ctrl 키는 중단의 의미를 가짐 

#딕셔너리의 원소 접근
"""
- {}가 아닌 []를 사용
- 키 값으로 변수를 주면 
a='name'
di = {a:'ice'} 
>>>'{name':'ice}

딕셔너리의 키로 변수 사용 가능
-단 변수는 immutable(불변) 데이터를 바인딩해야 함.
"""

"""
리스트의 범위를 넘어서는 인덱스에 값을 추가하면 오류남.
사전은 인덱스를 넘어서는 범위에 추가 가능


dict.get(1)과 dl[1]의 결과는 동일 
>>>'ice'

# dict.get() 메서드
  1) 딕셔너리의 요소의 값에 접근 용도
    : dict[‘key’]와 동일하나 해당 key가 없을 때 예외를 발생시키는 대신 None을 반환 

  2) 딕셔너리에 없는 키로 접근했을때 디폴트 값 반환
"""

my_key=input('키를 입력하세요> ')

my_dict = {
    1: 100,
    2: 'hello',
    30: True
}

score_dict={}

for i in range(10):
    score = input('학점(A,B 등)을 입력하세요 > ') #A
    score_dict[score] += score.get(score,0) +1##A라는 키가 딕셔너리에 없으면 0 반환 
    #score_dict['A']= 0+1
    #score_dict = {'A':1}
print(score_dict)

d = {
    'name':'홍길동',
    'job':'의적',
    'father':'홍판서',
    'age':'unknown'
}
print(d.keys())

#subscriptable = 색인할 수 있는

#range(100) >>>(0,100)
#list(range(100)) >>>[1,2,3,4......]

for key in d.keys():
    print('키: {}'.format(key))

for val in d.values():
    print('값: {}'.format(val))

#dict.items() :(키, 값)튜플 반환
print()
print(d.items())


#언패킹
for item in d.items():
    print(item[0], ":", item[1])
    
#튜플로 출력
for (key, value) in d.items():
    print(key, ':', value)

#확인문제
dict_a ={}
dict_a ={'name':'구름'}

del dict_a['name']

pets = [
    {"name": "구름", "age" : 5},
    {"name": "초코", "age" :3},
    {"name": "아지", "age" :1},
    {"name": "호랑이", "age" :1}
]

for pet in pets:
    print(pet['name'], str(pet['age'])+'살')

#강사님 버전
for (key, value) in d.items():
    print(key, value)

for pet in pets:
    print('{}, {}살').format(pet['name'], pet['age'])
    
numbers = [1,2,6,8,4,3,2,1,9,5,4,5,6,2,4,8,5,21,45,4,5,21,5,3,2,5,21,5,2,5]
counter = {}

for num in numbers: 
    if num in counter: #or counter.keys()
        counter[num]+=1
    else:
        counter[num] = 1

#sudo code#####################################################################33
#get은 이후에 중복으로 들어오는 값이 0으로 초기화되지 않고 기존에 있던 값에서 수정
for number in numbers:
    counter[number] = counter.get(number, 0)+1

print(counter)



type("문자열") is str #문자열인지 확인
type([]) is list
type({})

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ['베기', '세게 베기', '아주 세게 베기']

}


for key in character:
    print(['{} : {}'.format(key, character[key])])

#강사님
for key in character:
    value = character[key]

    if type(value) is dict:
        for k in value:
            print('{} : {}'.format(k, value[key]))
    elif type(value) is list:
        for v in value:
            print('{} : {}'.format(key,v))
    else:
        print('{} : {}'.format(key,value))
 """
 # 동등 연산자: is vs. ==
  - is 연산자: 변수에 저장된 주소가 같은 비교
               동일한 객체를 바인딩하는지 비교
  - == 연산자: 값이 같은지 비교
               주소가 다른 객체라도 값이 같으면 True
#문자열은 is나 ==에서 True로 뜨지만
#숫자형 예시 range(10)을 A와 B로 만들고 보니 ==은 True인데 is는 False가 됨 
 """   
