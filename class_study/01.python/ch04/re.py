#List 컴프리핸션 안에서 조건식
[ 표현식 for 변수 in 데이터 if 조건식]

l1 = list(range(10))
print('# l1 = {}'.format(l1))

#리스트 내포
#리스트 내포는 문법적으로는 if 만 지원 if-else는 지원하지 않음
# 대신 삼항연산자 사용하면 가능
l3 = [v*v for v in l1 if v% 2 == 1]
print('# l4 = {}'.format(l3) )

#List 컴프리헨션 안에서 조건식을 만족하지 않는 경우도 포함하고 싶을 때
#ex) 홀수면 '홀' 짝수면 '짝'으로 나타내는 리스트 생성
l4 = ['홀' if v % 2 ==1 else '짝' for v in l1]
print('# l4 ={}'.format(l4) )
#3항 연산자는 if는 불가 반드시 if else

#2진수를 10진수로 
int('1100', 2)

#반복문과 리스트 내포의 속도 차이를 보여주는 예제
l1 = list(range(1,10))
for v in l1:
    print('{} : {:b}'.format(v,v))

#위와 동일
for v in l1:
    print('{0} : {1:b}'.format(v))

#2번 문제########################################################################
#l1 = list(range(10))
output= [v for v in range(1, 101) if '{:b}'.format(v).count('0')==1]
for i in output:
    print("{} : {}".foramt(i, "{:b}".format(i)))
print("합계:", sum(output))

###
d1 = {v: '{:b}.format(v) for v in l1'}
#단, syntex:
#     {k:v for 변수 in 복합자료형}

#리스트 내포에서 []를 ()로 바꾸면 제너레이터 expression

