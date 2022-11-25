#https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    price_sum=0
    answer=0
    for c in range(1,count+1):
        price_sum+=(price*c)
    if price_sum > money:
        answer=price_sum-money
    else:
        answer=0
    return answer