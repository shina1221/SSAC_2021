#베달
"""
문제 : https://www.acmicpc.net/problem/2579

계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
<그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 
도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.

계단 오르는 데는 다음과 같은 규칙이 있다.

  1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
     즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
  2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다. 
  3. 마지막 도착 계단은 반드시 밟아야 한다.

따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 
모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 
구하는 프로그램을 작성하시오.

입력 
입력의 첫째 줄에 계단의 개수가 주어진다.
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

예제입출력
예제 입력 1             
    6                         
    10
    20
    15
    25
    10
    20

예제 출력 1
    75
"""

"""

#규칙
S(n) = max(S(n-1), S(n-2)+A(n))

def solution(data):
    if len(data) == 1: #입력된 배열길이가 1일 때 
        return data[0]  #첫번째 원소가 총합이 됨
    result = [data[0], max(data[0], data[1])]
    for i in range(2, len(data)):
        result.append(max(result[i-1], result[i-2]+ data[i])
    return result[-1]
"""
###시행착오#########################################################################################

#타 블로그 참고(https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

#값 입력받기
#문자열 n줄을 입력받아 리스트에 저장할 때
import sys
#계단의 수
n = int(sys.stdin.readline())
#계단 점수들
data = [int(sys.stdin.readline().strip()) for i in range(n)]

total=0
#연속되는 세 숫자의 위치와 값을 확인하기 위한 빈 딕셔너리 생성
mid_memo=dict()
#현재 리스트의 마지막 세 값이 연속하는 값인지 확인하기 위한 함수 정의
def ckeck three_numbers(mid_memo, total):
    #인덱스 내 세 수가 연속하는지 확인하고 연속되는 세 수일 경우에는
    #점점 수가 증가하는 추세이기 때문에 앞의 수 값(작은값)을 더해줬던 것을 제거하고 마지막 값을 선택해서 다시 반영 
    #if mid_ii[-3]+1==mid_ii[-2] and mid_ii[-2]+1==mid_ii[-1]:
    if int(list(mid_memo.keys())[-3:][0])+1==int(list(mid_memo.keys())[-3:][1]) and int(list(mid_memo.keys())[-3:][1])+1==int(list(mid_memo.keys())[-3:][2]):
        #이전에 더해줬던 값을 빼고
        total -= list(mid_memo.values())[-3:][0]
        #딕셔너리에서 해당 값 제외
        del(mid_memo[list(mid_memo.keys())[-3:][0]])
    return mid_memo, total
    
for i,ii in enumerate(data):
    if i == 0:
        total+=ii
#        now_ii=ii
    else:
#        now_ii=ii
        #세개가 연달아 중복되는지 확인하기 위한 리스트
        mid_ii = [] 
        #먼저 나온 값이 뒤에 나올 값보다 크거나 같을 경우
        if data[i]>=data[i+1]:
            total+=ii   #data[i]
            #추가한 값의 인덱스를 중간리스트에 추가
            mid_momo.append(i)
        else: 
            total+=data[i+1]
            #추가한 값의 인덱스를 중간 리스트에 추가
            mid_memo.append(i)

    result = [data[0], max(data[0], data[1])]
    for i in range(2, len(data)):
        result.append(max(result[i-1], result[i-2]+data[i]))
    return result[-1]    

#만약에 리스트안의 숫자위치 요소가 3개라면
#1번째 리스트를 중심으로 [i-1, i, i+1] 과 현재 리스트가 동일한지 파악

#만약 동일하다면 

        
        for second_i in range(2, len(data)):
            mid_ii.append(max(result[i-1], result[i-2]+ data[i])

#마지막 수와 마지막 수를 기준으로 -2번째 값과 비교해서  
        #-2번째 값이 더 크다면 
        if list(mid_memo.values())[-3:][0] >= list(mid_memo.values())[-3:][2]:
            total -= list(mid_memo.values())[-3:][0]
            del(mid_memo[list(mid_memo.keys())[-3:][2]])
