"""
#문제 : https://www.acmicpc.net/problem/10829

자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)

출력
N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

입출력 예
53         110101
"""
"""
2 53                             2 52                    2 1
  26 ...1                          26  ...0                0  ...1   
  13 ...0                          13  ...0
  6  ...1                           6  ...1
  3  ...0                           3  ...0 
  1  ...1      >>110101             1  ...1   >>110100
"""
#성공

from sys import stdin

def div(N):
    if N//2 == 0:  #1로 두었을 때 만약 N이 1이라면 검출하지 못하는 에러사항이 있었음
        trans_N.insert(0,str(N%2)) #나머지를 맨 앞에 추가
        answer = int(''.join(trans_N)) 
        print(answer)    
        return answer
    else:
        trans_N.insert(0,str(N%2)) #나머지를 맨 앞에 추가
        N=N//2 #N갱신
        div(N)

trans_N = []
N = int(stdin.readline().strip())
div(N)
#이하는 시행착오##########

from sys import stdin

trans_N = []
def div(N):
    if N//2 <= 0:  #마지막의 몫은 1 이하일 때
        trans_N.insert(0,str(N%2)) 
        trans_N.insert(0,'1') #맨 마지막의 몫은 항상 1이므로  
    else:
        trans_N.insert(0,str(N%2))
        N=N//2
        div(N)
    answer = ''.join(trans_N)  
    return answer

N = int(stdin.readline().strip())
div(N)

#

from sys import stdin

def div(N):
    if N//2 <= 1:  #마지막의 몫은 1일 때
        trans_N.insert(0,str(N%2)) 
        trans_N.insert(0,'1') #맨 마지막의 몫은 항상 1이므로
    else:
        trans_N.insert(0,str(N%2))
        N=N//2
        div(N)
    answer = int(''.join(trans_N))    
    return answer

trans_N = []
N = int(stdin.readline().strip())
div(N)

