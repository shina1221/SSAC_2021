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
#참고 https://girawhale.tistory.com/3
#참고 https://jinho-study.tistory.com/949
"""
마지막 계단을 반드시 밟아야 함
연속한 3개의 계단을 밟으면 안됨
크게 두가지 방식이 있음
          마지막 수
-3 -2 -1  n 
 0  _  0  0  
    0  _  0  

 0  _  0  0  
 0  0  _  0  

두가지 방식중에 더 큰 값 + 현재 밟는 계단 값 = 최고 점수 값
                           
                           -3 -2 -1  현재 값
                            0  _  0  0  
                               0  _  0  

##예시                          #적은 수 
10 20 15 25 10 20             | 10 20 15 25 10 20 
10                =10  1번째  | 10
10+20             =20  2번째  | 10 20 
   20+15          =35  3번째  | 10    15              (n-2)+n(현재수)와 (n-1)+n(현재수) 비교
10+20   +25       =55  4번째  | 10    15 25           (n-2)번째(까지의 최대) 총합+n과 (n-3)번째 총합+(n-1)+n 비교
10+20   +25+10    =65  5번째  | 10    15    10        (n-3)번째 총합+(n-1)+n과 (n-2)번째 총합+n 비교
10+20   +25    +20=75  6번째  | 10    15    10 20     (n-2)번째 까지의 총합+n과 (n-3)번째 총합+(n-1)+n 

#현재 위치값의 수는 항상 더한다
#앞에서 더한 총합은 이후에 영향을 미친다
#3번째에서 (0 _ 0) ( _ 0 0) 마지막 수는 반드시 더하기 때문에 앞의 두 수중 더 큰 것의 합을 채택
#(n-2)번째 값까지의 최대 총합+(n)현재값과 (n-3)번째 까지의 최대 총합+(n-1)번째값+(n)현재값이 반복해서 비교연산됨

#따라서 다음의 식이 나오게 됨
score[n] = max(score[n-3] + data[n-1], score[n-2]) + data[n]

#단 1번, 2번, 3번 계단은 0 _ 0 0 법칙이 성립되지 않으므로 미리 계산하고 시작
"""
##계단의 수
N = int(input())
#계단 점수들을 넣을 배열 생성
data=[-1]*301  #이렇게 안잡아두면 에러생김
#총합을 저장해둘 배열 생성
score=[-1]*301

#계단점수 삽입
for i in range(N):
    data[i] = int(input())

#첫번째 계단 총합
score[0] = data[0]
#두번째 계단 총합
score[1] = data[0]+data[1]
#세번째 계단 총합
#첫번째 계단과 두번째 계단중 더 큰 것 선택 + 현재의 계단
score[2] = max(data[0], data[1])+data[2]

#이미 세번째 계단까지 계산하고 시작하므로 4부터 시작
for j in range(3, len(data)):
    score[j] = max(score[j-3] + data[j-1], score[j-2]) + data[j]
    #print('score_i',score[i])
print(score[N-1])

###시행착오#########################################################################################

#런타임 에러

#값 입력받기
#문자열 n줄을 입력받아 리스트에 저장할 때
import sys
#계단의 수
N = int(sys.stdin.readline())
#계단 점수들
data = [int(sys.stdin.readline().strip()) for i in range(n)]
#점수배열 생성
score=[-1]*len(n)

#첫번째 계단 총합
score[0] = data[0]
#두번째 계단 총합
score[1] = data[0]+data[1]
#세번째 계단 최대 총합
#첫번째 계단과 두번째 계단중 더 큰 것 선택 + 현재의 계단
score[2] = max(data[0], data[1])+data[2]

#이미 세번째 계단까지 계산하고 시작하므로 4부터 시작
for i in range(3, len(data)):
    score[i] = max(score[i-3] + data[i-1], score[i-2]) + data[i]
    #print('score_i',score[i])
print(score[N-1])

"""
각 계단 점수의 배열을 data 해당 계단의 위치까지의 최고 점수의 값의 배열을 score
마지막 계단은 무조건 밟아야 하므로
2가지 경우중 큰값 +현재 계단의 값을 더한 값이 해당 칸의 score가 됨

0 0 _ 와 
0 _ 0 중에서 큰 것을 고름

0 0 _ 값이 더 크면 네번째 값을 더함
0 _ 0 값이 더 크면 네번째와 다섯번째 값을 비교해서 더 큰것을 더함

for i in range()

크게 위의 세가지 유형으로 나뉨


"""
##마지막 계단을 반드시 밟아야 하므로 마지막 계단부터 시작
#(마지막 수)현재로 부터 3개의 수까지 범위중 가장 작은 수를 제외 하고 인덱스에 추가
#다음 이전에 마지막 수로 존재하던 수를 기준으로 -2번쨰와 -3번째 수를 비교해 작은 값을 제외하고 인덱스를 딕셔너리에 추가
#마지막에 남은 수의 배열 인덱스가 1일때는 그대로 딕셔너리에 추가하고
# 마지막에 남은 수의 배열 인덱스가 2이상일 때는 위의 과정을 반복 

#만약 동일한 수가 연달아 존재할 경우 좀더 뒤에 나오는 수를 먼저 선택함
#이는 먼저나오는 수를 최대한 선택할 수 있게하기 위함
"""
ex) 10 20 15 25 10 20 
             25 +  20=45
        #3개의 수 중에서 가장 작은 수 제외
        #25기준 -1번째와 -2번째 중 작은 수 제외     
        20+          =65 #25기준
        #마지막 남은 배열의 개수가 1개라면 그대로 배열에 추가
    10+              =75

ex) 10 10 20 20 25 25 20
                   25+20=45 #동일한 수가 연속으로 나온다면 마지막 수를 우선 선택
             20+        =65
          20+           =85
    10+                 =95                
"""

#타 블로그 참고(https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

#값 입력받기
#문자열 n줄을 입력받아 리스트에 저장할 때
import sys
#계단의 수
n = int(sys.stdin.readline())
#계단 점수들
data = [int(sys.stdin.readline().strip()) for i in range(n)]

mid_memo=dict()
#거꾸로 시작
for i in range(len(data)-1,-1,-1):
    #print(i,data[i])
    #print(type(i), i)
    if i == len(data)-1:
        #마지막 계단은 반드시 밟아야 하므로 마지막 값을 추가하고 시작
        mid_memo[str(i)]=data[i]
        #다음 기준이 될 수를 계산해서 놔야 이어서 반복하므로 현재 미리 다음 수를 계산해 둠
        #이후 -2번째와 -3번째 값을 비교
        if data[i-1] >= data[i-2]:
            mid_memo[str(i-1)]=data[i-1]
            #다음 기준이 될 수 지정
            #집어넣은 수 다음 수를 뛰어 넘어서 기준을 지정해야 하므로 -3
            now_ind=i-3
        else:
            mid_memo[str(i-2)]=data[i-2]
            #다음 기준이 될 수 지정
            #집어넣은 수 다음 수 2개를 비교하기 위해 -2
            now_ind = i-2
    else:
        #인덱스를 맞추기 위해 continue            
        if now_ind != i:
            continue
        #현재 인덱스가 다음 기준이 될 수의 인덱스가 되었다면
        else:
            #-2번째와 -3번째 값 이어서 비교
            #단, 마지막 배열 남은 수가 1개 이하일 경우 그대로 합치고 종료
#삭제            if now_ind == 1:
#삭제               mid_memo['1']=data[1]
#삭제                mid_memo['0']=data[0]
#삭제                break
            if now_ind == 0:
                mid_memo['0']=data[0]
                #break
            #마지막으로 남은 배열의 수가 2 이상일 경우 비교를 계속해서 수행
            else:
                #이후 now_ind 값을 기준으로 한 -2번째와 -3번째 값을 비교
                #인덱스가 마이너스가 나올 수 있으므로
                #if now_ind>1:
                if data[i-1] >= data[i-2]:
                    mid_memo[str(now_ind-1)]=data[now_ind-1]
                    #다음 기준이 될 수 지정
                    now_ind=i-2
                else:
                    mid_memo[str(i-2)]=data[i-2]
                    #다음 기준이 될 수 지정
                    now_ind=i-3
    print('result: ', mid_memo, 'sum: ', sum(mid_memo.values()))


data=[10,10,20,20,25,25,20] 
#     10,   20,20,   25,20 
#95

#data=[10,20,20,25,25,20]
#         20,20,  25,20 
#85

#data=[10,20,15,25,10,20]
#      10,20,   25,   20        
#75

import sys
#계단의 수
n = int(sys.stdin.readline())
#계단 점수들
data = [int(sys.stdin.readline().strip()) for i in range(n)]

#빈딕셔너리 생성
mid_memo={}
#맨 마지막 수 반드시 밟아야 하는 계단은 추가하고 시작
mid_memo[str(len(data)-1)]=data[-1]
now_ind=len(data)-1
total = data[-1]
#아래에 해당하는 인덱스의 값이 딕셔너리에 포함되면 (_00) 유형의 인덱스 모양을 포함할 수 없음 (_00)(0) 이런식으로 세 수가 연속되기 때문
#check_ind=now_ind-2
#따라서 data[i-2]에 해당하는 값이 딕셔너리에 선택될 경우 
#(0_0)혹은 (00_) 두가지 유형중 하나의 합만 선택할 수 있게됨

#그외로 i-1인덱스가 딕셔너리에 포함되는 경우는 
#(00_), (0_0), (_00)유형중 가장 큰 총합을 선택할 수 있음

#거꾸로 시작
for i in range(len(data)-1,1,-1):
    check_ind=now_ind-2
    #이후 -2번째와 -3번째 값을 비교
    if len(data)>=6:
        if data[i-1] >= data[i-2] and i == now_ind:
            mid_memo[str(i-1)]=data[i-1]
            #다음 수 3개중에서 가장 작은 수를 제외한 두 수를 채택
            #data[i-3:i-6]
            total+=max(data[i-3]+data[i-4], data[i-3]+data[i-5], data[i-4]+data[i-5])
            #다음 기준이 될 수 지정
            #집어넣은 수 다음 수를 뛰어 넘어서 기준을 지정해야 하므로 -3
            now_ind=i-3        
        if data[i-2] > data[i-1] and i == now_ind:
            mid_memo[str(i-2)] = data[i-2]
            #다음 기준이 될 수 지정
            #집어넣은 수 다음 수 2개를 비교하기 위해 -3
            now_ind =i-3
            #-3번째는 반드시 선택하나
            #중간에 겹치는 숫자가 나올 수 있는 가능성이 있으므로 
            #-2번째와 -1번째 중 더 큰 수를 선택하게 됨
    else: #len(data)>6     

    #중간 메모장을 확인해서 연속되는 두 수가 이미 선택되었는지 확인
    #연속되는 두개의 인덱스가 이미 선택되었다면   
    elif list(mid_memo.keys())[-1]+1 == list(mid_memo.keys())[-2]:
            #바로 다음 수는 연속되는 세번째 수이므로 추가할 수 없으므로 한칸 건너뛴 수를 추가
                mid_memo[str(i-3)]=data[i-3]
                #해당 수를 기준 수로 받음
                now_ind = i-3
            else:  
            #연속되는 두개의 수가 아니라면
            #-2번째 수와 -3번째 수를 비교해서 더 큰 수를 추가
                if data[i-2] >= data[i-3]:
                    mid_memo[str(i-2)]=data[i-2]
                else:
                    mid_memo[str(i-3)]=data[i-3]
                #그 다음의 수를 기준 수로 받음
                   now_ind = i-4                          

    
    else:
        #인덱스를 맞추기 위해 continue            
        if now_ind != i:
            continue
        #현재 인덱스가 다음 기준이 될 수의 인덱스가 되었다면
        else: #now_ind==i
            #-2번째와 -3번째 값 이어서 비교
            #단, 마지막 배열 남은 수가 1개 이하일 경우 그대로 합치고 종료
            if now_ind == 0:
                mid_memo['0']=data[0]
                #break
            #마지막으로 남은 배열의 수가 2 이상일 경우 비교를 계속해서 수행
            else:
                #이후 now_ind 값을 기준으로 한 -2번째와 -3번째 값을 비교
                #인덱스가 마이너스가 나올 수 있으므로
                #if now_ind>1:
                if data[i-1] >= data[i-2]:
                    mid_memo[str(now_ind-1)]=data[now_ind-1]      
                if data[i-2] > data[i-1]:
                    mid_memo[str(now_ind-2)]=data[now_ind-2]
            now_ind=i-3
            #중간 메모장을 확인해서 연속되는 두 수가 이미 선택되었는지 확인
            #연속되는 두개의 인덱스가 이미 선택되었다면
            if list(mid_memo.keys())[-1]+1 == list(mid_memo.keys())[-2]:
            #바로 다음 수는 연속되는 세번째 수이므로 추가할 수 없으므로 한칸 건너뛴 수를 추가
                mid_memo[str(i-3)]=data[i-3]
                #해당 수를 기준 수로 받음
                now_ind = i-3
            else:  
            #연속되는 두개의 수가 아니라면
            #-2번째 수와 -3번째 수를 비교해서 더 큰 수를 추가
                if data[i-2] >= data[i-3]:
                    mid_memo[str(i-2)]=data[i-2]
                else:
                    mid_memo[str(i-3)]=data[i-3]
                #그 다음의 수를 기준 수로 받음
                   now_ind = i-4                          
                else: #data[i-2] >= data[i-1]
                    mid_memo[str(now_ind-2)]=data[now_ind-2]
                    #중간 메모장을 확인해서 연속되는 두 수가 이미 선택되었는지 확인
                    #연속되는 두개의 인덱스가 이미 선택되었다면
            ???        if list(mid_memo.keys())[-1]+1 == list(mid_memo.keys())[-2]:
                        #바로 다음 수는 연속되는 세번째 수이므로 추가할 수 없으므로 한칸 건너뛴 수를 추가
                        mid_memo[str(i-3)]=data[i-3]
                        #해당 수를 기준 수로 받음
                        now_ind = i-3
                    else:  
                        #연속되는 두개의 수가 아니라면
                        #-1번째 수와 -2번째 수를 비교해서 더 큰 수를 추가
                        if data[i-1] >= data[i-2]:
                            mid_memo[str(i-1)]=data[i-1]
                        else:
                            mid_memo[str(i-3)]=data[i-3]
                        #그 다음의 수를 기준 수로 받음
                        now_ind = i-4                          

    print('result: ', mid_memo, 'sum: ', sum(mid_memo.values()))
    
answer=sum(mid_memo.values())    
print(answer)




                    #중간 메모장을 확인해서 연속되는 두 수가 이미 선택되었는지 확인
                    #연속되는 두개의 인덱스가 이미 선택되었다면
                    if list(mid_memo.keys())[-1]+1 == list(mid_memo.keys())[-2]:
                        #바로 다음 수는 연속되는 세번째 수이므로 추가할 수 없으므로 한칸 건너뛴 수를 추가
                        mid_memo[str(i-3)]=data[i-3]
                        #해당 수를 기준 수로 받음
                        now_ind = i-3
                    else:  
                        #연속되는 두개의 수가 아니라면
                        #-2번째 수와 -3번째 수를 비교해서 더 큰 수를 추가
                        if data[i-2] >= data[i-3]:
                            mid_memo[str(i-2)]=data[i-2]
                        else:
                            mid_memo[str(i-3)]=data[i-3]
                        #그 다음의 수를 기준 수로 받음
                        now_ind = i-4      

##

total=0
#연속되는 세 숫자의 위치와 값을 확인하기 위한 빈 딕셔너리 생성
mid_memo=dict()
#현재 리스트의 마지막 세 값이 연속하는 값인지 확인하기 위한 함수 정의
def ckeck_three_numbers(mid_memo):#, total):
    #인덱스 내 세 수가 연속하는지 확인하고 연속되는 세 수일 경우에는
    #점점 수가 증가하는 추세이기 때문에 앞의 수 값(작은값)을 더해줬던 것을 제거하고 마지막 값을 선택해서 다시 반영 
    #if mid_ii[-3]+1==mid_ii[-2] and mid_ii[-2]+1==mid_ii[-1]:
    if int(list(mid_memo.keys())[-3:][0])+1==int(list(mid_memo.keys())[-3:][1]) and int(list(mid_memo.keys())[-3:][1])+1==int(list(mid_memo.keys())[-3:][2]):
        #이전에 더해줬던 값을 빼고
#        total -= list(mid_memo.values())[-3:][0]
        #딕셔너리에서 해당 값 제외
        del(mid_memo[list(mid_memo.keys())[-3:][0]])
    return mid_memo #, total

##
for i,ii in enumerate(data):
    #세개가 연달아 중복되는지 확인하기 위한 리스트
    #먼저 나온 값이 뒤에 나올 값보다 크거나 같을 경우
    if data[i]>=data[i+1]:
        #total+=ii   #data[i]
        #추가한 값의 인덱스를 중간리스트에 추가
        mid_memo[str(i)]=ii
    if data[i+1]>=data[i]: 
        #추가한 값의 인덱스를 중간 리스트에 추가
        mid_memo[str(i)]=ii
    if len(mid_memo)>=3:    
        print('mid_memo0', mid_memo)
        mid_memo=ckeck_three_numbers(mid_memo)
        print('check_three_numbers: ', 'mid_memo', mid_memo)   #, ' total', total)
print('mid_memo', mid_memo)
result = sum(mid_memo.values())
print('result:', result)

##

for i,ii in enumerate(data):
    if i == 0:
#        total+=ii
        mid_memo['0']=ii
    else:
#        now_ii=ii
        #세개가 연달아 중복되는지 확인하기 위한 리스트
 #       mid_ii = [] 
        #먼저 나온 값이 뒤에 나올 값보다 크거나 같을 경우
        if data[i]>=data[i+1]:
#            total+=ii   #data[i]
            #추가한 값의 인덱스를 중간리스트에 추가
            mid_memo[str(i)]=ii
        else: 
#            total+=data[i+1]
            #추가한 값의 인덱스를 중간 리스트에 추가
            mid_memo[str(i)]=ii
        mid_memo=ckeck_three_numbers(mid_memo)
        print('check_three_numbers: ', 'mid_memo', mid_memo)   #, ' total', total)
result = sum(mid_memo.values())
print('result:', result)
##

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






