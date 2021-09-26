#실행 ctrl+F5
import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \

#if else elif
#else 키워드는 항상 if 구문의 마지막에
#elif 키워드는 필요한 만큼 얼마든지 사용

#Flase로 변환되는 값(Truth Value Testing)
#상수 중에서는 None 혹은 False를 false로 정의
#수치데이터 중 0으로 되는 숫자들(0, 0.0, 0j, Decimal(0), Fraction(0, 1)) False로 정의
#빈 시퀀스, 빈 컬렉션: '',"",(),[],{}, set(), range()객체는 False로 정의

#pass 키워드
#-빈 코드 블록이 필요할 때
#다른 언어에서는 {}
#파이썬은 빈 코드 블록을 허용하지 않음(반드시 문장이 존재해야 함)

#사용자에게 태어난 연도를 입력받아 띠를 출력하는 프로그램
str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input) % 12

if birth_year ==0:
    print('원숭이')
elif birth_year ==1:
    print('닭')
elif birth_year ==2:
    
