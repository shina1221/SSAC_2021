"""
문제 : https://www.acmicpc.net/problem/2745

B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 팩토리얼 진법 숫자를 10진법으로 읽은 값을 출력한다.

입출력 예

입력                            진법        출력
Z      Z     Z     Z     Z       36          60466175
36**4  36**3 36**2 36**1 36**0

35*(36**4)       +   35*(36**3)       +   35*(36**2)        +    35*(36**1)         +   35*(36**0) =60466175
N-1 * (N*자릿수) +   N-1 * (N*자릿수) +   N-1 * (N*자릿수)  +    N-1 * (N*자릿수)   +   N-1 * (N*자릿수)
      len(str(N))    len(str(N))-1        len(str(N))-1-1        len(str(N))-1-1-1      len(str(N))-1-1-1-1    

#2진수 표현 1,0으로만 하고 2는 없음
#36진수도 마찬가지 35까지만 표현
#0부터 시작하기 때문

#[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
number_dict = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,'A':11,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'H':19,'J':20,'K':21,'L':22,'M':23,'N':24,'O':25,'P':26,'Q':27,'R':28,'S':29,'T':30,'U':31,'V':32,'W':33,'X':34,'Y':35,'Z':36}
             # 1번째가 0
"""

#타인 코드 참조
#https://claude-u.tistory.com/462 참조

#테스트 케이스 중에 공백까지 계산해야하는 테스트케이스가 있던듯 함.
#따라서 딕셔너리가 아닌 유니코드값을 기준으로 계산해야 했음
#부적절한 테스트 케이스가 포함된 듯

from sys import stdin

N, B = stdin.readline().strip().split(' ')

B = int(B)
lN = len(N)-1
result = 0

for i, j in enumerate(N):
    try:
        if int(j): #숫자일 경우
            result += int(j) * B ** lN
    except: #알파벳 혹은 공백일 경우   
        result += (ord(j)-55) * B ** lN
    lN -= 1

print(result)

"""
ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.
ord('A') >>> 65    -55    10
ord(' ') >>> 32    -55    #공백까지도 계산해야 하는듯  #공백까지 계산해야 통과함 
ord('Z') >>> 90    -55    35
"""

#이하는 시행착오
###############################################################################################################################
number_dict = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,'A':11,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'H':19,'J':20,'K':21,'L':22,'M':23,'N':24,'O':25,'P':26,'Q':27,'R':28,'S':29,'T':30,'U':31,'V':32,'W':33,'X':34,'Y':35,'Z':36}
             # 1번째가 0

from sys import stdin

#재귀함수 사용(로직 성공)
N, B= 'ZZZZZ', 36
cnt=0
result=0
def mul(cnt, N, B):
    global result
    #모든 수에 대해 진법 계산이 끝났으면
    if N == '':
        return result
    #맨앞의 수부터 진법계산    
    else:    
        #진법의 자릿수 -1 만큼 제곱
        cnt = len(N)-1
        result+=(int(number_dict[N[0].upper()])-1) * B ** cnt
        #cnt-=1
        #점점 계산할 자릿수를 하나씩 줄임
        N=N[:-1]
        print(cnt, result, N, B)
        mul(cnt, N, B) 

mul(cnt, N, B)

"""
#vs code상 실행시 이렇게 함수바깥에 못 놓음
N, B = stdin.readline().strip().split(' ')
result=0
def(x,y):
    pass
"""

################################################################################

N, B= 'ZZZZZ', '36'
result=0
def mul(cnt, N, B):
    #global 안해주면 바깥에 있는 result =0으로만 남음
    #마찬가지로 result를 전역변수로 썼기 때문에 파라미터로도 인자로도 쓸 수 없음
    global result
    B= int(B)
    #모든 수에 대해 진법 계산이 끝났으면
    if N == '':
        print('B:', B) 
        #작업종료
        return 0
    #맨앞의 수부터 진법계산    
    else:    
        #진법의 자릿수 -1 만큼 제곱
        cnt = len(N)-1
        result+=(int(number_dict[N[0].upper()])-1) * B ** cnt
        #점점 계산할 자릿수를 하나씩 줄임
        N=N[:-1]
        mul(cnt, N, B) 

#결과확인    
mul(cnt, N, B)    
result

#### while문 활용  #잘 돌아가는데 런타임 에러
while True:
    #한줄로 받은 값을 각각 
    #B진법수 N과 B진법을 한줄로 받아 공백기준으로 나눠서 객체할당
    N, B = stdin.readline().strip().split(' ')
    result=0
    mul(cnt, N, B)
    print(result)    
    if result > 1000000000:    
        break


#런타임 에러때문에 재수정

N, B = stdin.readline().split()
B=int(B)
result=0

for i in N:
    #모든 수에 대해 진법 계산이 끝났으면
    if N == '':
        print(result)
    #맨앞의 수부터 진법계산    
    else:    
        #진법의 자릿수 -1 만큼 제곱
        cnt = len(N)-1
        result+=(int(number_dict[N[0].upper()])-1) * B ** cnt
        #cnt-=1
        #점점 계산할 자릿수를 하나씩 줄임
        N=N[:-1]
        print(cnt, result, N, B)
        mul(cnt, N, B) 

mul(cnt, N, B)

#결과확인    
mul(cnt, N, B)    
result
    
##################
#런타임 에러
from sys import stdin

N, B = stdin.readline().split(' ')

number_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'H':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

def mul(N, B, result):
    lN = len(N)-1
    result=0
    B=int(B)
    for s_i in N:
        result  += number_dict[s_i.upper()] * (B ** lN)
        lN -= 1
    return result

#mul(N, B, result)

if mul(N, B, result) > 1000000000:
    pass
else:
    print(mul(N, B, result))


##################
#계산하는 과정에서 10만이 넘으면 틀렸다고 하는 가능성을 고려
#거꾸로 계산해 나가기
#13%에서 막힘

from sys import stdin

N, B = stdin.readline().split(' ')

number_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'H':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

lN = 0
result=0
B=int(B)

try:
    for s_i in N[::-1]:
        if result <= 1000000000:
            result  += number_dict[s_i.upper()] * (B ** lN)
            lN += 1
        else:
            break
except:
    pass

if lN==len(N): 
    print(result) 
else:
    pass

#숫자와 문자열로 케이스를 나눠서 합산
#ord(c)는 문자의 유니코드 값을 돌려주는 함수.
# 수정버전 통과안됨

from sys import stdin

N, B = stdin.readline().split(' ')

number_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'H':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

lN = len(N)-1
result=0
B=int(B)

if len(B) < 10:
    print(int(N))
else:
    for s_i in N:
        try:
            result  += number_dict[s_i.upper()] * (B ** lN)
            lN -= 1
        except:
            pass
    print(result)


## 다른사람 풀이 참조
#https://claude-u.tistory.com/462 참조
N, B = input().split()
B = int(B)
result = 0

for i, j in enumerate(N):
    try:
        if int(j):
            result += int(j) * B ** (len(N)-i-1)     
            print(i,j,len(N)-i-1, result)
    except: #문자열이면
        result += (ord(j)-55) * B ** (len(N)-i-1)  
        print(i,(ord(j)-55),len(N)-i-1, result, 'check')
        
print(result)



        