# 두 정수 사이의 합
def solution(a, b):
    if a<b:
        answer = sum(list(range(a,b+1)))
        return answer
    else:
        answer = sum(list(range(a,b-1,-1)))
        return answer        

# 수박수박수박수박수박수?
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

# 서울에서 김서방 찾기
def solution(seoul):
    ans_i = seoul.index('Kim')
    answer = '김서방은 {}에 있다'.format(ans_i)
    return answer

# 약수의 합
def solution(n):
    answer=0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer

# 문자열 내 p와 y의 개수
#1차 시도 실패
def solution(s):
    for ss in s:
        if ss.count('p')==ss.count('y'):
            answer = True
        elif ss.count('p')==ss.count('y')==0:
            answer = True
        else:
            answer = False
    return answer

#2차 시도 
#대문자와 소문자 구별을 안함을 빠뜨리고 있었음
s = "pPoooyY"
ss= "kjkjkjkjkjkjk"
def solution(s):
    if s.count('p')+s.count('P')==s.count('y')+s.count('Y'):
        answer = True
    else:
        answer= False
    return answer

#같은 숫자는 싫어

#1차 #결과값은 반환되나 에러뜸
for i in range(len(arr)-2): # 0부터 
    if arr[i] == arr[i+1]:
        arr.pop(i)

#2차 //2일 걸림
def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(len(arr)-1): 
        if arr[i] == arr[i+1]:
            pass
        else:
            answer.append(arr[i+1])
            #print(arr[i], arr[i+1])    
    return answer

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
    
#직사각형 별찍기############################ 안됨
#whitespace란, 띄어쓰기(' '), 탭('\t'), 엔터('\n') 까지, 포괄적으로 이야기 하는것이다.
#이 whitespace를 제거하기 위해선, strip 함수를 사용하면 된다.
#n번 시도해도 안되서 다른 솔루션 참조

#입력받은 숫자를 split을 활용해 띄어쓰기 기준으로 나누고 map으로 int로 변환한 뒤 a,b로 선언
#받은 값의 양옆 공백을 strip으로 제거
a, b = map(int, input().strip().split(' '))

for _ in range(b):
    print('*'*a)

#평균 구하기
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

#행렬의 덧셈
#zip 사용해서 풀어볼 것
#append 메서드 자체는 return값으로 None을 돌려준다.
#>>> list(zip([1, 2, 3], [4, 5, 6]))
#[(1, 4), (2, 5), (3, 6)]

#1차 시도 실패
arr1= [[1,2],[2,3]]
arr2 = [[3,4], [5,6]]
#return [[4,6],[7,9]]
def solution(arr1, arr2):
    #answer= []
    #answer_f=[]
    for j in range(len(arr1)):  #j= [1,2]  k= [3,4] 
        #print(list(zip(arr1[j],arr2[j])))  
        ing_list = list(zip(arr1[j],arr2[j]))
        #answer = map(list(zip(arr1[j],arr2[j])))
        for k in range(len(ing_list)):
            answer[k]= sum(list(answer[k]))
    return answer
    # sum(list(k))
    # answer_f.append(sum(list(k)))
    # answer = answer.insert(j,(list(zip(arr1[j],arr2[j]))))  #  [4,6]
    # return answer

solution(arr1, arr2)
# 2차  / 2시간 걸림
def solution(arr1, arr2):
    answer=[]
    for j in range(len(arr1)):
        a = zip(arr1[j],arr2[j])
        #print(a)
        result=[]
        for k in a:   
            #print(sum(list(k)))
            result.append(sum(list(k)))
        #print('result:', result)
        answer.append(result)
    return answer 

solution(arr1, arr2)

#짝수와 홀수	
def solution(num):
    if num%2==0:
        answer = 'Even'
    else: 
        answer = 'Odd'
    return answer

#자릿수 더하기	
def solution(n):
    n=str(n)
    answer = sum([int(i) for i in n])
    return answer

#최대공약수와 최소공배수 //3일 걸림
def solution(n,m):
    dict_i = {}
    answer= []
    #인자들의 순서가 바뀌었을 때를 고려
    if n < m:
        max_i = m
        min_i =n
    elif n == m:
        max_i=m
        min_i =n
    else:
        #n>m
        max_i = n
        min_i = m
    dict_i[str(min_i)] = []
    dict_i[str(max_i)] = []
    #각 숫자별 약수구하기
    for i in range(1, min_i+1):
        if min_i >=i and min_i%i==0:
            dict_i[str(min_i)].extend([i, int(min_i/i)])
    for i in range(1, max_i+1):
        if max_i >=i and max_i%i==0:
            dict_i[str(max_i)].extend([i, int(max_i/i)])
    #print('dict_i:'. dict_i)
    #중복약수 제거
    #'list' object is not callable에러
    #이전에 다른 문제 풀면서 같은 이름으로 선언된 함수명을 여기서 또 사용해서 일어난 에러
    #아마 람다함수에서 문제를 일으킨듯 
    #함수명으로 자주 쓰이는 단어는 변수명으로 사용하지 않도록 한다.
    set_list_min=list(set(list(map(lambda x : int(x), dict_i[str(min_i)]))))
    set_list_max=list(set(list(map(lambda x : int(x), dict_i[str(max_i)]))))
    set_list_max.sort()
    set_list_min.sort()
    #print('max:', set_list_max)
    #print('min:', set_list_min)           
    #겹치는 약수 산출
    #재귀적 자료구조에 위와 같은 처리를 해 하나의 단일 값으로 반환하는 것을
    #fold라고 하며, 파이썬에서는 이 기능을 functools모듈의 reduce라는 함수로 지원
    from functools import reduce
    #GCM(Greatest Common Measure) //최대공약수###############################
    #겹치는 약수 중에서 가장 큰 약수
    #교집합
    #GCD=list(set(set_list_min).intersection(set_list_max))[-1]
    inter_l=list(set(set_list_min).intersection(set_list_max))
    inter_l.sort()
    #print('inter_l(교집합):', inter_l)
    #공통된 약수들의 리스트에서 가장 큰 약수 추출 
    GCM=inter_l[-1]
    #print('최대공약수:', GCM)
    #LCM(largest common multiple) //최소공배수################################
    #합집합
    union_l=list(set().union(set_list_min,set_list_max))
    union_l.sort()
    #리스트 내 모든 약수들을 곱하기 위한 함수 
    def multiply(list_l):
        LCM = reduce(lambda x, y: x * y, list_l)
        return LCM
    #한쪽 리스트가 다른 한쪽 리스트에 포함되는 경우(포함관계)
    # =합집합 한게 최대수의 리스트와 길이가 같다면
    if len(union_l)==len(set_list_max):
        LCM = union_l[-1]
    #1만 공통 약수라면(=1 제외하고 겹치는 약수가 없다면) 리스트의 가장 큰 수만 추출해 곱한다
    #if len(list(set(set_list_min).intersection(set_list_max)))==1:
    elif len(inter_l)==1:
        #LCM = multiply(union_l)
        LCM = set_list_max[-1]*set_list_min[-1]
    #각 리스트의 약수들이 일부만 겹치는 경우
    #최대공약수와 최대공약수로 나누고 나온 몫까지 곱함
    else:
        LCM = int(GCM * (max_i/GCM) * (min_i/GCM))
    answer=[GCM, LCM]
    return answer

#정수 제곱근 판별 //이틀걸림
#1차 실패 테스트13에서 걸림
def solution(n):
    import math
    import re
    if '.0' in str(math.sqrt(n)) :
        answer = (int(math.sqrt(n))+1)**2
    else:
        answer=-1
    return answer

#2차 시도 안됨
def solution(n): 
    import math
    if '-' not in str(math.sqrt(n)) and '.0' in str(math.sqrt(n)):
        answer = (int(math.sqrt(n))+1)**2
    else:
        answer=-1
    return answer

#3차 성공 #7.06532 이런 경우도 있어서 맨 마지막을 기점으로 서치
def solution(n):
    import math
    if '.0' in str(math.sqrt(n))[-2:] :
        answer = (int(math.sqrt(n))+1)**2
    else:
        answer=-1
    return answer
