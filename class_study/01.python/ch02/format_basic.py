string_a = "{}".format(10)
print(string_a)

# 중괄호만 쓰는데 공백들어가면 오류
# string_a = "{   }".format(10)

format_a ="{}만 원".format(5000)
format_b ="파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)
format_d = "{} {} {}".format(1,"문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

#포맷팅의 괄호안에 들어가는 인자는 그 수가 같아야 한다 적거나 많으면 
#:d는 정수를 특정칸에 출력/folat형이나 문자열은 에러뜸
#소수점보다 큰 정수값은 다 출력됨
output_a = "{:d}".format(52)

#기호붙여 출력하기 
output_a = "{:+d}".format(+52)
output_a = "{:+d}".format(-52)

#조합해보기
output_h = "{:+5d}".format(52) #     +52
output_h = "{:+05d}".format(52) #+0052

#float
output_a = "{:f}".format(52.273)

#소수점 아래 자릿수 지정
#3f면 셋째자리 이하 소수점이 반올림되서 나옴, 2f면 둘째자리까지 반올림해서 나옴
output_a = "{10.f}".format(52.273)

#{:d}, {:f}
#숫자에서 정수부분은 지정된 자릿수보다 크더라도 모두 출력되고  
#소수점 이하는 반올림되어 출력됨

#{}추가설명
"""
1) 위치지정
    -{position}: 인자의 위치값(정수)
    -'{0}은(는) {1}보다 강하다.format('펜','칼')
"""

#f-string(3.6버전이상에서 가능)
obj1='펜'
obj2='칼'
f'{obj1}은(는) {obj2}보다 강하다'

a='hello'
a.upper()
a.lower()

#strip() 공백제거
#lstrip() 왼쪽의 공백 제거
#rstip() 오른쪽 공백제거

#strip메서드는 공백 말고도 원하는 글자만 남기는데 사용할 수도 있음.
#인자가 없음 whitespace 제거
#인자를 문자열로 받으면: 해당 문자열을 구성하는 문자들을 제거
