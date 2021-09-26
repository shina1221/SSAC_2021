#두 정수 사이의 합

def solution(a, b):
    if a<b:
        answer = sum(list(range(a,b+1)))
        return answer
    else:
        answer = sum(list(range(a,b-1,-1)))
        return answer
    
        

#수박수박수박수박수박수?
def solution(n):
    answer = ''
    answer=list(answer)
    for cont in range(n):
        if cont%2==1:
            answer.append('수')
            answer= ''.join(answer)
        else:
            answer.append('박')
            answer= ''.join(answer)
    return answer

#서울에서 김서방 찾기
def solution(seoul):
    ans_i = seoul.index('Kim')
    answer = '김서방은 {}에 있다'.format(ans_i)
    return answer

#약수의 합
def solution(n):
    answer=0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer

#문자열 내 p와 y의 개수##############################

def solution(s):
    for ss in s:
        if ss.count('p')==ss.count('y'):
            answer = True
        elif ss.count('p')==ss.count('y')==0:
            answer = True
        else:
            answer = False
    return answer

#같은 숫자는 싫어#############################3
arr = [[1,1,3,3,0,1,1],[4,4,4,3,3]]   
for ar in arr:
    for ar_i in ar:
        print(ar_i)

def solution(arr):
    answer=[]
    for arr_li in arr:
        for arr_i in len(arr_li):
            print(arr_i)

for arr_li in arr:
    for arr_i in range(len(arr_li)):
        print(arr_i)

def solution(arr):
    answer=[]
    for arr_li in arr:
        for arr_i in range(len(arr_li)):
            #지금 위치 기준으로 뒤에 같은 수가 있다면 pop
            if arr_li[arr_i] == arr_li[arr_i+1]:
                #answer.remove(arr_li[arr_i])
            else:
                pass
    answer=arr_li
    return answer


arr = [[1,1,3,3,0,1,1],[4,4,4,3,3]]   

for arr_li in arr:
    for arr_i in range(len(arr_li)):
        #지금 위치 기준으로 뒤에 같은 수가 있다면 pop
        if arr_li[arr_i] == arr_li[int(arr_i)+1]:
            answer= arr_li.remove(arr_li[arr_i])
            print(answer)
    
#가운데 글자 가져오기
def solution(s):
    if len(s)%2 == 1:
        answer=s[len(s)//2]
    else:
        before_s =s[(len(s)//2)-1:(len(s)//2)+1]
        answer = ''.join(before_s)
    return answer

#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []        
    for add_1 in range(1, n+1):
        answer.append(add_1*x)
    return answer
    
#직사각형 별찍기############################3
def square_star(n,m):
        print(n*m'*'.split)

#평균 구하기
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

#행렬의 덧셈
#zip 사용해서 풀어볼 것

#짝수와 홀수	


#자릿수 더하기	


#최대공약수와 최소공배수	


#정수 제곱근 판별

