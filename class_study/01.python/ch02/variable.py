pi = 3.14159265
r=10

print("원주율=", pi)
print("반지름=", r)
print("원의 둘레=", 2*pi*r)
print("원의 넓이=", pi*r*r)

#input('무엇을 넣을것인가요')함수
#데이터 형 변환(데이터 타입 변환)
#-type Conversion, Type Cast, Type Casting

string_a = input("input_A>")
int_a = int(string_a)

int_b = int(input("input_B> "))
#int_b = int(string_b)

#print("문자열 자료",  string_a + string_b)
print("숫자자료:", int_a +int_b)

#마무리
str_input = input("숫자입력>")
num_input = int(str_input)

print()
print(num_input, "inch")
print((num_input * 2.54), "cm")

#
num_input = int(input('숫자 입력>'))
print('\n', num_input, 'inch', sep='')
print(num_input*2.54, 'cm')

#5번
str_input = input("원의 반지름 입력>")
num_input = int(str_input)
print()
print("반지름: ", num_input)
print("둘레: ", 2*3.14 * num_input)
print("넓이: ", 3.14*num_input**2)

#변수 스왑 : 바꾸는 것
#두 변수의 내용을 서로 바꾸는 연산
#[일반적, 다른 프로그래밍 언어]: 임시 변수 필요, 문장 3개 필요
#파이썬: 문장 1개로 충분
#x,y=y,x

a= input("문자열 입력a")
b= input("문자열 입력b")
print(a,b)
c=0
c=a
a=b
b=c
print(a,b)

a,b=b,a
print(a,b)

#2-4 포맷팅
print('price is %d and name is %s' % (100,'ice'))
print('Price is {}, and name is {}'.format(100, 'ice'))
output = 'Price is {}, and name is {}' 
output.format(100, 'ice')

#포맷팅 출력: 틀을 갖추고 변하는 부분만 데이터로 치환해서 출력

#코드 블록에 이름 붙인것
## 코드 블록에 이름 붙인 것
#  - 예전에는 ‘루틴’ → ‘서브루틴’
#  - ‘루틴’ -> ‘프로그램’ -> ‘서브프로그램’ -> 반환값 있는: 함수
#                                              반환값 없는: 프로시저(procedure) 

## 문자열을 날것 그대로 표현하고 싶을 때
#  - 문자열 앞(따옴표 왼쪽)에 r  → raw string

