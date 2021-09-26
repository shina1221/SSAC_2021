#확인문제
#리스트 평탄화
def flatten(data):
    #재귀함수 활용
    output = []
    if type(data) != list: #받은 data가 리스트 타입이 아니라면
        return output.append(data)
    else:
        for element in data:
            next(data)
            print(element)
            output += flatten(element)
            return output
            
example= [[1,2,3],[4,[5,6]],7,[8,9]]
print('원본 :', example)
print('변환 :', flatten(example))

##################################33

def flatten(data):
    output=[]
        for element in data:
            if type(element) == list:
                output += flatten(element)
            else:
                output.append((element))
        return output

##################33
#강사님 버전 semi

#alt+shitf+커서 로 다중 커서 만들고 내가 수정하고자 하는 단어 전체 수정 가능
min_sitting = 2
max_sitting = 10
total_people = 100
memo = {}
def count_table_sitting(people_left, num_sitting):
    key = str([people_left, num_sittng])    
    #재귀함수는 종료조건 필요
    if key in memo:
        return memo[key]
#    people_left -= num_sitting #들여쓰지 않아도 되는가?
    if people_left <0: #무효이므로 리턴
        return 0
    if people_left ==0 : #유효하므로 수를 세기 위해 1 리턴
        return 1
        
    #재귀처리
    #새 테이블에 최소인원으로 앉힘
    if num_sitting > max_sitting:
        return 0
    count = count_table_sitting(people_letf-min_sitting, min_sitting)
    #if count == 0 and people_left_sitting >0 and num_sitting <10:
    #    count = count_table_sitting(people_letf, num_sitting+1) 
    #메모화 처리
    memo[key] = count

    #종료
    return count + count_table_sitting(people_letf, num_sitting+1)


#풀이버전
least_p = 2
maximum_p = 10
total_p = 100
memo = {}

def pro(left_p, sit_p): #남은사람 수, 앉힌 사람 수
    key = str([left_p, sit_p])
    #종료조건
    if key in memo:
        return memo[key]
    if left_p < 0: #무효이므로 0 리턴
        return 0
    if left_p == 0: #유효하므로 수를 세기 위해 1 리턴        
        return 1
    #재귀처리
    count =0
    for i in range(sit_p, maximum_p+1):
        count += + pro(left_p - i, i)

    #메모화 처리
    memo[key] = count
    #종료
    return count
print(pro(total_p, least_p))


k={'[2,0]':0, '[2,2]':1, '[2,3]':2}

#수정 내버전
least_p = 2
maximum_p = 10
total_p = 10#100
memo = {}
total_count = 0

def problem(left_p, sit_p): #남은사람 수, 앉힌 사람 수
    key = str([left_p, sit_p]) #키 값으로 리스트 못 넣음 서치 기준을 남은사람 수와 앉힌 사람 수로 할 것임
    #종료조건
    if key in memo: # 메모 딕셔너리에 키 값이 있으면 출력하고 종료
        return memo[key]
    if left_p  < 0 : #남은 사람이 음수라면 계산 종료
        #print(left_p, sit_p)
        return 0
    if left_p == 0: #남은 사람이 0명이라면 계산 종료
        # print(left_p, sit_p)
        return 1
    # 재귀처리 
    for sep in range(least_p,maximum_p+1): #0,1일때를 제외하고 for문으로 경우의 수를 계산
        problem((maximum_p-sep),sep)#최대사람수에서 숫자를 빼가며 키값을 만들어 냄
        if memo[str([(maximum_p-sep),sep])] in memo: #키값이 이미 존재한다면 숫자 카운팅
            total_count += memo[str([(maximum_p-sep),sep])]
            #global total_count += memo[str([(maximum_p-sep),sep])]  #수식문제
                    #global total_count += int(len(memo[key])/2)  #갯수가 홀수일 경우때문에 int추가 #왜 안돼지?
    # 메모화처리
        if  maximum_p>10:
            continue
        if key not in memo: #memo 딕셔너리에 키값이 없다면 키값 추가 
            memo[sep]=memo[sep].append(str(key)) 
    #종료
    return total_count
print(problem(total_p, least_p))

##강사님 2차

"""
(남은인원수, 앉힌사람 수)

N=2, 앉힐수 있는 최대 사람수 =10
(2,2), (2,3), (2,4), ..., (2,9), (2,10)
N=3
(3,2), (3,3), (3,4), ..., (3,9), (3,10)
(3,2) --> (1,2)

"""
#강사님 버전 semi2

#alt+shitf+커서 로 다중 커서 만들고 내가 수정하고자 하는 단어 전체 수정 가능
min_sitting = 2
max_sitting = 10
total_people = 8
memo = {}

level = -1
def count_table_sitting(people_left, num_sitting):
    
    global level
    level += 1
    key = str([people_left,num_sitting])    
    
    print(' '*level*2 +key)
    #재귀함수는 종료조건 필요
    if key in memo:
        return memo[key]
#    people_left -= num_sitting
    if people_left <0: #무효이므로 리턴
        level-= -1
        return 0
    if people_left == 0: #유효하므로 수를 세기 위해 1 리턴
        level-= -1
        return 1
        
    #재귀처리
    count = 0
    for sitting in range(num_sitting, max_sitting+1):
        print(' '*level*2 + str([people_left, sitting]))
        count += count_table_sitting(people_left-sitting, sitting)

    #메모화 처리
    memo[key] = count

    #종료
    level-= -1    
    return count

"""
설명
total_people:2

함수(2,2)
key: '[2,2]'
count :0
[for] sitting: 2 <== range(2,11) --> 2 <== i < = 10
    count = count + 함수(2-2, 2)
                    (0,2)
함수(0,2)
key: '[0,2]'
return 1
count = count + 1

for문 3
함수(2-3, 3) .....


N= 6
(6,2) -> (4,2) -> (2,2) -> (0,2) ==> 1
               -> (2,3) -> (-1,2) ==> 0   #(2,3)
               -> (2,4) -> (-2,2) ==> 0
                ...
               -> (2,10) -> (-8,2) ==> 0
      -> (4,3) -> (1,2) -> (-1,2) ==> 0 #이 과정안하고 바로 (1,3)으로 감
               -> (1,3) -> (-2,2) ==> 0 #앞에서 (2,3)을 거침 
               ...
               -> (1,10) -> (-9, 2) ==> 0
      -> (4,4) -> (0,2) -> 1
      ..
(6,4) -> (2,2) -> (-2,2) ==> 0

N=7 (2,2,3)
    (2,5)
    (3,4) 
    (4,4)

N=8 (2,2,2,2)
    (2,2,4)
    (2,3,3)
    (2, 6)
    (3, 5)
    (4, 4)
    (8)
 ####앉히는 수가 기점이 됨
            
""" 
#####
<확인문제>

1번) 
강사의 풀이
def flatten(data):
    output = []
    for element in data:
        if type(element) == list:
            output += flatten(element)
        else:
            output.append(element)
    return output


2)번: 키 중복을 해결해야 함
min_sitting = 2
max_sitting = 10
total_people = 6
memo = {}
 
level = -1
 
def count_table_sitting(people_left, num_sitting):
 
    global level
    level += 1
 
    key = str([people_left, num_sitting])
    if key in memo:
        return memo[key]
    
    if people_left < 0:
        level -= 1
        return 0
    if people_left == 0:
        level -= 1
        return 1
 
    #재귀 처리
    count = 0
    for sitting in range(num_sitting, max_sitting+1):
        print(' '*level*2 + str([people_left, sitting]))
        count += count_table_sitting(people_left-sitting, sitting)
 
    #메모화 처리
    memo[key] = count
 
    #종료
    level -= 1
    return count
 
print(count_table_sitting(total_people, min_sitting))
 

