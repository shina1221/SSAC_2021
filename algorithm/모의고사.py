"""
1번 수포자가 찍는 방식 [1,2,3,4,5]*n 반복
2번 수포자가 찍는 방식 [2,1,2,3,2,4,2,5]*n 반복
3번 수포자가 찍는 방식 [3,3,1,1,2,2,4,4,5,5]*반복
문제의 정답을 대조해 가장 많이 맞춘 사람을 선출(단 공동 포함)

모든 사람들의 답을 정답지와 비교해가며 채점. (완전탐색)

[]
|   **1번 수포자의 경우**   |     **2번 수포자의 경우**       |     **3번 수포자의 경우**   |   
|        (5씩 반복)        |          (8씩 반복)            |          (10씩 반복)        |   
| :----------------------- | :---------------------------: | ------------------------- :|
|  (순서)         (찍은값)  |  (순서)              (찍은값) |  (순서)           (찍은값)   | 
| 5n+1번째 수%5=1     1     | 8n+1번째 수%8=1 (홀)    2     | 10n+1번째 수%10=1    3      |
| 5n+2번째 수%5=2     2     | 8n+2번째 수%8=2 (짝)    1     | 10n+2번째 수%10=2    3      |
| 5n+3번째 수%5=3     3     | 8n+3번째 수%8=3 (홀)    2     | 10n+3번째 수%10=3    1      | 
| 5n+4번째 수%5=4     4     | 8n+4번째 수%8=4 (짝)    3     | 10n+4번째 수%10=4    1      |
| 5n+5번째 수%5=0     5     | 8n+5번째 수%8=5 (홀)    2     | 10n+5번째 수%10=5    2      |
|                          | 8n+6번째 수%8=6 (짝)    4      | 10n+6번째 수%10=6    2     |
|                          | 8n+7번째 수%8=7 (홀)    2      | 10n+7번째 수%10=7    4     | 
|                          | 8n+8번째 수%8=0 (짝)    5      | 10n+8번째 수%10=8    4     |
|                          |                               | 10n+9번째 수%10=9    5     |
|                          |                               | 10n+10번째 수%10=0   5     |
| :----------------------- | :---------------------------: | --------------------------:|
| (특징)                   | (특징)                         | (특징)                     |    
| 5로 나누고 난 후          | 8로 나누고 난 후                | 10으로 나누고 난 후         |  
| 나머지 값으로             | 추가로 나머지를 2로 나눴을 때    | 나온 나머지를 기준으로       |
| 찍을 값 결정              | 나머지가 1(홀)일 때는 2         | 일정 수 구간마다            |
|                          | 그 외는 8로 나눈 뒤 나머지       | 찍을 값 결정               |
|                          | 값에 따라서 찍을 값 결정         |                           |

>>>반복기준 수로부터 얼마나 떨어진 값인지 인덱스를 기준으로 
   for문을 통해 모든 수를 정답과 대조(완전탐색)
#실제 코드 
"""
def solution(answers):
    #First 첫번째 수포자
    def find_first_now(i):
        first_now=0
        if i % 5 !=0:
            first_now=i%5
        else:
            first_now=5
        return first_now
    first_cnt=0
    #Second 두번째 수포자
    def find_second_now(j):
        second_now=0
        #8로 나눠 홀수 번째 수들이 모두 2일 때
        if (j % 8) %2 ==1:
            second_now=2
        #짝수번째 수들은 8로 나눈 나머지
        if j%8 == 2:
            second_now=1        
        if (j%8) == 4:
            second_now=3                
        if (j%8) == 6:
            second_now=4               
        if (j%8) == 0:
            second_now=5               
        return second_now
    second_cnt=0
    #Third 세번째 수포자
    def find_third_now(k):
        third_now=0
        #끝자리수 기준으로 숫자 나뉨
        if k%10==1 or k%10==2:
            third_now=3
        if k%10==3 or k%10==4:
            third_now=1
        if k%10==5 or k%10==6:
            third_now=2
        if k%10==7 or k%10==8:
            third_now=4
        if k%10==9 or k%10==0:
            third_now=5
        return third_now
    third_cnt=0
    #완전탐색
    for i in range(len(answers)):
        if answers[i]==find_first_now(i+1):
            first_cnt+=1
    for j in range(len(answers)):
        if answers[j]==find_second_now(j+1):
            second_cnt+=1
    for k in range(len(answers)):        
        if answers[k]==find_third_now(k+1):
            third_cnt+=1
    max_cnt=0
    total_dict={}
    total_dict['1']=first_cnt
    total_dict['2']=second_cnt
    total_dict['3']=third_cnt
    answer=[int(k) for k, v in total_dict.items() if v == max(total_dict.values())]
    answer.sort()
    return answer
