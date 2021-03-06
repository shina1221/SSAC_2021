1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
예시)
가로의 숫자를 입력하시오 : 4
세로의 숫자를 입력하시오 : 4
★★★★
★★★★
★★★★
★★★★

#가로
width_len=int(input('가로의 숫자를 입력하시오:')) 
#세로
length_len=int(input('세로의 숫자를 입력하시오:'))

for ll in range(length_len):
    print('*' * width_len)

2. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오

width_len = int(input('가로길이를 넣으시오'))
length_len= int(input('높이를 넣으시오'))

def triangle(width_len, length_len):
    return width_len*length_len*0.5

triangle(width_len,length_len)

3. 아래와 같이 별이 찍히게 출력하시오
숫자를 입력하세요 : 
    ★
    ★★
   ★★★
  ★★★★
  ★★★★★  
  ★★★★
   ★★★
    ★★
    ★

number=int(input('숫자를 입력하세요:'))
cnt=0

while cnt<number:
    print(('*'*(cnt+1)).center(5,' '))
    if cnt==4:
        for j in range(3,-1,-1):
            print(("*"*(j+1)).center(5," "))
    cnt+=1

4 .1부터 100까지의 수의 합을 계산하던 중에 합이 1000 이상일 때, 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오

total_sum=0
cnt=0
while total_sum<=1000:
    cnt+=1
    total_sum+=cnt
    
print(cnt)

5. 정수를 입력했을때 짝수인지 홀수인지 핀별하는 코드를 작성하시오

num= int(input('숫자를 넣으시오'))
if num%2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

6. 리스트 메서드 중 하나를 이용하여 아래의 리스트를 ABCD순으로 정렬하시오.
namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']

namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
namelist.sort()
namelist

7. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. (리스트 split 과 슬라이싱 활용)

Rr_num= input('주민등록번호를 입력하시오')
Rr_list=Rr_num.split("-")

if Rr_list[1][0]==1 or Rr_num[7]=='1':
    print('남자입니다')
elif Rr_list[1][0]==2 or Rr_num[7]=='2':
    print('여자입니다')  

8. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고 파일 이름만 추가 리스트에 저장하시오.
file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
last_file=[]
for i in file:
    last_file.append(i.split('.')[0])
last_file   

9. 다음 리스트에서 알파벳의 갯수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for i in a:
    if len(i)==7:
        print(i)

10. 리스트 메서드 중 하나를 이용하여 아래의 리스트에 '화성'이라는 요소를 삽입하시오.
출력 전 리스트 : planet =['태양','수성','금성','목성','토성','천왕성','해왕성']
출력 후 리스트 : planet =['태양','수성','금성','화성','목성','토성','천왕성','해왕성']

planet =['태양','수성','금성','목성','토성','천왕성','해왕성']
planet.insert(3,'화성')
planet

11.점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 점수를 입력했을때 해당 학점이 출력하게 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

test_score=int(input('점수를 입력하시오'))
if test_score in range(81,101):
    print('A')
elif test_score in range(61,81):
    print('B')    
elif test_score in range(41,61):
    print('C')    
elif test_score in range(21,41):
    print('D')    
elif test_score in range(0,21):
    print('E') 

12. 최대공약수 및 최소공배수를 구하는 함수를 구현하시오.

a=int(input('첫번째 수를 입력해 주세요'))
b=int(input('두번째 수를 입력해 주세요'))
def common(a,b):
    a_measures=[i for i in range(1,a+1) if a%i==0]
    b_measures=[i for i in range(1,a+1) if b%i==0]

    #print(a_measures)
    #print(b_measures)

    #greatest common factor
    gcf=[i for i in a_measures if i in b_measures][-1]
    #print(gcf)

    #Least Common Multiple
    lcm = gcf* a//gcf * b//gcf
    #print(lcm)
    
    return gcf, lcm

common(a,b)

13.Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
print 기능(print) # 잔액이 ( ) 원 입니다.

money = int(input('현재 카드 잔액'))
                 
class Card():
    def charge(money):
        add_money= int(input('충전할 금액을 넣으세요'))
        money+=add_money
        print(f"잔액이 {money}원입니다.")
    def consume(money):
        minus_money= int(input('소비할 금액을 넣으세요'))
        money-=minus_money
        print(f"잔액이 {money}원입니다.")

Card.charge(money)
Card.consume(money)

14. 년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하시오.

from datetime import date
print('date(2021, 10, 30) 형식으로 작성하시오')
today= date(2021, 10, 30)
print(today)
today.weekday()

if today.weekday()==0:
    print('월요일')
if today.weekday()==1:
    print('화요일')
if today.weekday()==2:
    print('수요일')
if today.weekday()==3:
    print('목요일')
if today.weekday()==4:
    print('금요일')
if today.weekday()==5:
    print('토요일')
if today.weekday()==6:
    print('일요일')

15 계산기 기능을 하는 Calculator 클래스를 만드시오.
cal = Calculator()
<입력>
print(cal.Add(10,20))
print(cal.Min(10,20))
print(cal.Mul(10,20))
print(cal.Div(10,20))

num1=int(input('첫번째 수를 입력하시오'))
num2=int(input('두번째 수를 입력하시오'))

class cal():
    def Add(num1,num2):
        return num1+num2
    def Min(num1,num2):
        return num1-num2
    def Mul(num1,num2):
        return num1*num2
    def Div(num1,num2):
        return num1/num2
    
print(cal.Add(10,20))
print(cal.Min(10,20))
print(cal.Mul(10,20))
print(cal.Div(10,20))        

16. Gorila 라는 클래스를 생성하시오.
1. 바나나를 먹는 기능 : eat
2. 바나나가 뱃속에 몇 개 남았는지 확인하는 기능 : check
3. 소리지르는 기능 : shout
4. 걷는 기능 :  walk

banana_num=int(input('보유한 바나나갯수를 입력하시오'))
eat_num=int(input('먹은 바나나 갯수를 입력하시오'))

class Gorila():
    def eat(eat_num):
        global banana_num
        banana_num=banana_num-eat_num
        return eat_num
    def check(banana_num):
        return banana_num
    def shout():
        print('shout')
    def walk():
        print('walk')
        
print(Gorila.eat(eat_num))
print(Gorila.check(banana_num))
Gorila.shout()
Gorila.walk()

17. Gun 이라는 클래스를 생성하시오.
1. 충전 기능 : charge
2. 쏘는 기능 : shoot
3. 남아있는 총알 갯수 확인 기능 : check

bullet=0
charge_num=5

class Gun():
    def charge(charge_num):
        global bullet
        bullet+=charge_num
    def shoot():
        global bullet
        bullet-=1
    def check():
        global bullet
        return bullet

bullet=0
Gun.charge(charge_num)
print(Gun.check())
print('=======================')
Gun.shoot()
Gun.shoot()
Gun.check()  

18. 아직 정렬되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복하여 정렬하는 것을 삽입정렬이라고 합니다. 주어진 리스트를 삽입정렬함수(insert_sort)를 생성하여 오름차순으로 정렬하시오.
list=[6,2,3,7,8,10,21,1]

list_a=[6,2,3,7,8,10,21,1]

for i in range(1, len(list_a)):
    for j in range(i):
        if list_a[i] < list_a[j]:
            list_a.insert(j,list_a.pop(i))
            print(list_a)
list_a

19 .앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을 경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다. 주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
list=[4,3,2,1,8,7,5,10,11,16,21,6]

list_b=[4,3,2,1,8,7,5,10,11,16,21,6]

for i in range(len(list_b)-1):
    for j in range(len(list_b)-1):
        if list_b[j]>list_b[j+1]:
            list_b[j+1],list_b[j] = list_b[j],list_b[j+1]
            print(list_b)

list_b

20. 팩토리얼은 1부터 n까지 연속한 숫자의 곱이라 합니다. 팩토리얼을 함수(factorial)로 구현하는데 재귀함수를 이용하여 구현하시오.

def factorial(num):
    if num>1:
        return num * factorial(num-1)
    else:
        return 1
    
factorial(5)
