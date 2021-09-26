#예외처리

"""
[Ch.06-1 p.272] 구문 오류와 예외

# 오류(Error)와 예외(Exception)
  * 오류: 프로그램이 실행되지 않거나 작동이 중단되는 모든 상황
    cf.) 논리적 오류: 프로그램이 중단되지는 않는데 우리가 원하는 대로 작동하지 않는 경우
  * 오류의 종류
    1) 프로그램 실행 전 오류: 컴파일러의 경우 → 보통 구문 오류
       : compile error , compile-time error, compliation-time error
    2) 프로그램 실행 중 오류
       : run-time error ⇒ 예외(Exception)

#예외의 싸이클
 발생(Raise) --> 잡기(Trapping) --> 처리(handling)

 #예외의 발생
 * 시스템, 운영체제, 인터프리터가 발생
 * 프로그래머, 프로그램이 발생시킬 수도 있음 >>raise

# 예외의 발생
  * 자동 발생: 시스템, 운영체제, 인터프리터가 발생
  * 수동 발생: 프로그래머, 프로그램이 발생시킬 수도 있음 ⇒ raise

# 디버깅(Debugging)
  * 프로그램의 각종 오류를 해결하는 작업

# EOF : END OF FILE // EOL : END OF LINE

#예외 처리(Exception Handling)0
1)기본 예외 처리: 조건문 이용
2)고급 예외 처리: try 구문

# finally가 유의미하게 사용되는 경우
  1) try 구문 안에서 return ⇐ 함수, 메서드
     → return 문이 실행되기 전에 finally 실행
  2) 반복문 안의 try 구문 내에서 break
     → break 문으로 반복문을 빠져나오기 직전에 finally 실행

try:
    예외가 발생할 가능성이 있는 코드
except:
    예외가 발생했을 때 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    무조건 실행할 코드
"""

try:
    number = int(input('원의 반지름을 정수로 입력하세요 > '))
    print('원의 반지름', number)
except:
    print('무언가 잘못되었습니다.')

print('program must go on')

#######################################################################
l1 = ['52', '273', '스파이', '103']
l2= [element for element in l1 if element.isdigit()]
print(l1)
print(l2)

try:
    file = open('info.txt', 'w') #이 문장이 완전히 실행된게 아님 r이면 낫디파인드 에러 뜸
    abc=abc+1
    print('무사히 실행')
except:
    print('파일에 무언가 문제가 발생')
file.colse()

##########################3

with open('info01.txt', 'r') as file:
    try:
        abc= abc+1
        print('무사히 실행')

    except:
        print('무엇인가 잘못됨')

#file.close()
print(file.closed)


############################
#실행 자체가 되지 않는 코드가 구문오류(syntex error), 실행중에 발생하는 오류는 예외(exception)
output = 10 +"개" #예외
int('안녕하세요') #예외
cursur.close) #구문오류
[1,2,3,4,5][10] #예외

#try + else 구문은 구문오류가 발생하며 진행할 수 없음
#반드시 except웨에 else가 와야함.



