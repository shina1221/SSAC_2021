#https://school.programmers.co.kr/learn/courses/30/lessons/12951
#문자열.upper()
#문자열.lower()

#컴프리헨션 if else
#[i for i in range(5) if i%2==0]
#[i for i in range(5) if i%2==0 if i%4==0]
#[i if i%2==0 else 'odd' for i in range(5)]

s="for the last week"
#공백문자가 연속해서 나올 수 있습니다.
#예외 "for the last   week"

def solution(s):
    answer = ' '.join([ss[0].upper() + ss[1:].lower() if ss!='' else '' for ss in s.split(' ')])
    return answer

#다른 사람의 풀이
#title()
#문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

def Jaden_Case(s):
    return s.title()
print(Jaden_Case("3people unFollowed me for the last week"))