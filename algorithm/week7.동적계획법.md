## 동적계획법

# 동적계획법
- 다이나믹 프로그래밍(Dynamic Programming, DP)라고도 불리며, 하나의 큰 문제를 여러 개의 공통되는 작은 문제로 나누어서 작은 문제의 정답들을 결합하여 알고리즘을 푸는 과정
- 규칙을 찾는 문제

- 점화식
수열에서 n번째 항을 이전에 나온 항들로 나타낸 공식

- bottom up 방법
작은 문제에서 큰 문제로 반복문 호출

- top down 방법
큰 문제에서 작은 문제로 재귀 호출

# 피보나치 수열
n=[0,1,2,3,4,5,6,7]
  [1, 1, 2,3 ,5 8, 13, 21]

A(n) = A(n-1) + A(n-2), A(0)=1, A(1)=1

# 피보나치 수열 코드
def fib(n):
    fibList = [1,1]
    for i in range(2, n+1):
        fibList.append(fibList[i-2]+fibList[i-1])
    return fibList[-1]

# Top Down 방식
A(n) = A(n-1) + A(n-2), A(0)=1, A(1)=1
                    fib(n)
      fib(n-1)                  fib(n-2)
fib(n-2)    fib(n-3)      fib(n-3)    fib(n-4)
 fib(0)      fib(0)        fib(1))     fib(1)                           
       fib(1)                     fib(0)
   1     1     1             1      1      1   

# 즉 피보나치 수열은 0번째 수열과 1번째 수열의 결합으로 이뤄짐

def fib(n):
    if n==0 or n==1:
        reuturn 1
    else:
        return fib(n-1) +fib(n-2)

# 문제! 
 -피보나치 수열 값을 하나 생성하기 위해선 많은 양의 연산이 들어가게 되고 
 그와 동시에 계산중복이 이뤄짐

#문제를 해결하기 위한 방법: 메모이제이션()
-앞에서 했던 계산을 저장해두고 필요할 때 불러서 활용해 중복계산을 방지하는 방법 
-배열 혹은 해시를 활용하는 것이 핵심

memo = {0:1, 1:1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result

# 동적계획법 예시
data = [3,4,5,6,1,2,5]
이웃하지 않는 숫자들의 합의 최댓값은?
3을 골랐을 때 4는 못고르고 6을 골랐다면 바로 1을 선택할 수 없음

            n=0    n=1    n=2      n=3       n=4        n=5        n=6  
                                           #전전값8  #전전값10  #전전값10
배열        [3]   [3,4]  [3+5,4]  [6+4,8]  [8+1,10]  [10+2,10]  [12, 10+5]  
합 최댓값    3      4       8        10       10         12         15  

이웃하지 않은 최대 총 합은 15

data= [A(0),A(1),A(2),A(3),A(4),A(5),A(6)]
# 둘 중에 더 큰쪽이 값이 됨
A(0)  S(0),0+A(1)  S(1),S(0)+A(2)  S(2),S(1)+A(3)  S(3),S(2)+A(4)  S(4),S(3)+A(5)  S(5),S(4)+A(6)
S(0)      S(1)          S(2)            S(3)            S(4)           S(5)             S(6)

# 규칙
S(n) = max(S(n-1), S(n-2)+A(n))

def solution(data):
    if len(data) == 1: #입력된 배열길이가 1일 때 
        return data[0]  #첫번째 원소가 총합이 됨
    result = [data[0], max(data[0], data[1])]
    for i in range(2, len(data)):
        result.append(max(result[i-1], result[i-2]+ data[i])
    return result[-1]