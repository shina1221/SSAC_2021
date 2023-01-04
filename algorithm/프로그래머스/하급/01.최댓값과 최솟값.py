#https://school.programmers.co.kr/learn/courses/30/lessons/12939
#'??'.join(list)
#문자열.split('구분자', amxsplit=분할횟수)
#문자열.replace('바꿀문자열','바뀌는 내용')
#풀이
s="-1 -2 -3 -4"
def solution(s):
    answer =str([min(map(int, s.split(' '))), max(map(int, s.split(' ')))]).replace(',', '')[1:-1]
    return answer

#다른 사람의 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
