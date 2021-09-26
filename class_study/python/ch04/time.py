import time
time.time()

number = 0

target_tick = time.time()+5
while time.time() < target_tick:
    number+=1

#출력합니다
print("5초동안 {}번 반복했습니다.".format(number))

#break
i =0

while True:
    print("{}번째 반복문입니다.".format(i))
    i=i+1
    input_text = input("종료하시겠습니까 Y/N:")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다")
        break

#2번
key_list = ["name", "hp", "mp", "level"]
value_list = ['기사', 200, 30, 5]
character = dict
#내가한거(틀림)
for i in key_list:
    character[i]=value_list[i]
#그냥 요소를 그대로 받아서 하기때문에 value_list의 요소 인덱싱이 불가
#강사님
for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

#list(range(10, 2, -2))라고 한다면 마지막 수인 2는 포함되지 않음


print(character)
#3번
#내가한거
limit = 10000
i=1
sum_value = 0
while sum_value<10000:
    sum_value+=i
    i+=1
print('{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.'.format(i-1, limit, sum_value))

#강사님


#내가한거
limit = 10000
i=1
sum_value = 0
while sum_value<= limit:
    sum_value+=i
    i+=1
print('{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.'.format(i-1, limit, sum_value))


#4번
#내가한거 (20-30분 걸림)
max_value = 0
a=0
b=0

for i in range(0,100,1):
    a=i
    b=100-i
    now_value = a*b #현재값
    if now_value > max_value: #현재값과 과거값비교
        max_value=now_value
        print(max_value)  
print("최대가 되는 경우: {0} * {1} = {2}".format(a,b, max_value))

        
#강사님
max_value = 0
a=0
b=0

for j in range(1,100):
    j=100-1
    #최댓값 구하기
    mult = i*j
    if mult > max_value:
        max_value = mult
        value= [i,j]
        #a=i
        #b=j

print("최대가 되는 경우: {} * {} = {}".format(value[0],value[1], max_value)
print("최대가 되는 경우: {} * {} = {}".format(a,b, max_value)

#변수의 Scope, 변수의 Lifecycle
"""
-변수는 선언 또는 초기화될 때 접근 가능
-선언된 코드 블록을 벗어나면 삭제됨
-파이썬의 경우
    :함수가 종료되면 함수의 변수인 지역변수(로컬변수)는 삭제되지만
    복합문 내에서 선언된 지역 변수는 복합문의 코드 블록을 벗어나도 사라지지 않음.
"""

#reversed 함수의 반환객체
# - 이터레이터 : 제너레이터의 일종
# - 순회하면서 값을 소진
#만약 재사용하고싶다면 리스트로 만들던지 해야함.
#이터레이터로 출력시 next
#next(리스트, '끝')하면 순환이 끝나고나서 계속 끝 출력
#리스트 컴프리핸션
"""
-리스트 리터럴 구문 안에 for 문 포함
- 반복문에서 list.append()를 사용하는 방법보다 속도가 빠름
"""

#홀수만 뽑아서 제곱
values=[1,2,3,4,5,6,7,8,9]
r=2
l3 = [value**2 for value in values if value % r ==1]
l3
#if는 사용가능하나 else는 불가능

#리스트 거꾸로
revalue = values[::-1]
#콤마가 없으면 튜플이 아님
test = ( "i say " "mu " "you say " "yaho")
test

#문자열 연결
':'.join(test)

#item 메서드 enumerate 함수