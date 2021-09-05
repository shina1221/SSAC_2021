"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

예제입력
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

예제입력에 대한 출력
3 0 0 1 2 0 0 2

"""
#내가 보유한 숫자카드의 수
N=int(input())
#ex)10

#내가 가진 숫자카드의 수를 넘는 수가 입력될 수 있음
n_list=list(map(int, input().split(' ')))
#ex) 6 3 2 10 10 10 -10 -10 7 3 3 3 3 3

#내가 입력한 숫자에서 내가 가진 카드 수 만큼 숫자를 가지기 위해 del
#n_list_len= len(n_list)
#left_slice=n_list_len-N

#만약 보유카드수와 입력된 카드수가 동일할 경우
#굳이 이렇게 처리하는 이유는 카드수가 0일 때 아래의 코드로 실행하면 -0이 뜨면서 index 오류가 나기 때문
if len(n_list)-N==0:
    pass
#보유카드수와 입력된 숫자의 수가 다를 경우 보유카드 수 만큼 카드를 가짐
else:
    del n_list[-(len(n_list)-N):]
n_list.sort()

#내가 비교할 카드 수
M=int(input())
#ex)9
#비교할 수 입력
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10 10 10 10 10 10

#위와 마찬가지로 비교할 카드수를 넘는 수가 입력될 수 있으므로 아래의 코드로 동일하게 처리
if len(m_list)-M==0:
    pass
else:
    del m_list[-(len(m_list)-M):]

#비교할 숫자에 대한 딕셔너리 생성
dict_num = {}
for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

#탐색하는데 불필요한 작업을 최대한 배제하는 식으로 알고리즘 구성
for n in range(N): #내가가진 카드 요소 만큼 반복
    if str(n_list[n]) not in dict_num: #내가 찾고자 하는 숫자가 dict에 없다면 세지 않아도 되는 수이므로 
        continue
    elif dict_num[str(n_list[n])] != 0: #만들어둔 체크리스트 딕셔너리에 0이외의 탐색 숫자가 있다면 이미 카운팅 한 것이므로 
        continue
    elif dict_num[str(n_list[n])] == 0: #만들어든 체크리스트에 현재의 탐색숫자가 0이라면 (탐색해 보지 않은 것이므로) #이후에도 동일한 숫자가 나올 수 있긴 하지만
        left, right = 0, N-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적(현 줄 타인코드 참고)
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                left=mid+1         

#M개의 숫자도 중복된 숫자가 있을 수 있음(간과해서 오래 걸린 부분)
#[str(dict_num[str(m)]) for m in m_list  if str(m) in dict_num]
print(' '.join([str(dict_num[str(m)]) for m in m_list  if str(m) in dict_num]))

#출력 시간측정

#print(' '.join(str(dict_num[str(x)]) if str(x) in dict_num else '0' for x in m_list[:M]))
#0.02601 sec
#print(' '.join([str(n) for n in dict_num.values()]))
#0.01500 sec

#sorting 시간측정 

#12.20963 sec
#n_list=list(map(int, input().split(' ')))
#n_list.sort()
#13.42049 sec

#하단은 시도 시행착오
##################################3
# 1차 시도 타임오버
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')[:N]
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')[:M]
total_count=''
total=''
for i in m_list: #기준이 되는 숫자 선출
    cnt=0  #카운드하기 위해 초기화   
    total= total+' '+str(sum([cnt+1 for j in n_list if i==j]))

#2차 타임오버
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')[:N]
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')[:M]
total_count=''
for i in m_list: #기준이 되는 숫자 선출
    cnt=0  #카운드하기 위해 초기화   
    for j in n_list: 
        if i==j: #비교리스트에 찾고자 하는 값이 있으면
            cnt+=1 #그 수만큼 카운팅
    total_count=total_count+' '+str(cnt)

#3차 타임오버
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')[:N]
n_list=list(map(lambda x : int(x), n_list))
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')[:M]
m_list=list(map(lambda x : int(x), m_list))
#수를 세기위해 딕셔너리 생성
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
#이분탐색을 위해 sorting
m_list.sort()

#스트링 형태로 돌면 10의 경우 1로 시작하기에 sorting시 2보다 먼저나옴
#따라서 int로 변환해주고 돌아야 함

#이분탐색
for i in range(len(n_list)):
    find_num=int(n_list[i]) #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
#        print(mid, 'real:', m_list[mid])
#        print('find_num', find_num, 'left', m_list[left], 'right', m_list[right])
        if int(m_list[mid]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[left]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[right]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif  int(m_list[mid]) > find_num :
            right=mid-1
        elif int(m_list[mid]) < find_num :
            left=mid+1

dict_num.values()
total_list=list(dict_num.values())
total_count=''
for i in total_list:
    total_count=total_count+' '+str(i)

#4차 
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')[:N]
n_list=list(map(lambda x : int(x), n_list))
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')[:M]
m_list=list(map(lambda x : int(x), m_list))
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
m_list.sort()
for i in range(len(n_list)):
    find_num=int(n_list[i]) #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
        if int(m_list[mid]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[left]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[right]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif  int(m_list[mid]) > find_num :
            right=mid-1
        elif int(m_list[mid]) < find_num :
            left=mid+1

dict_num.values()
total_list=list(dict_num.values())     
total_count=''                               
for i in total_list:
    total_count=total_count+' '+str(i)       #여기서 시간 오래걸림
print(total_count)

#5차
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')
n_list=list(map(lambda x : int(x), n_list))
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')
m_list=list(map(lambda x : int(x), m_list))
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
m_list.sort()
for i in range(len(n_list)):
    find_num=int(n_list[i]) #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
        if int(m_list[mid]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[left]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[right]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif  int(m_list[mid]) > find_num :
            right=mid-1
        elif int(m_list[mid]) < find_num :
            left=mid+1

total_list=list(dict_num.values())
total_str='0'*2*len(total_list)
total_list1=list(map(lambda x: str(x), total_list))
" ".join(total_list1)

#6차
N=int(input('보유하고 있는 카드의 수'))
int_string_N=input('공백으로 수를 기준합니다 수를 넣어주세요.')
n_list=int_string_N.split(' ')
n_list=list(map(lambda x : int(x), n_list))
M=int(input('비교할 기준이 되는 카드의 수'))
int_string_M=input('공백으로 수를 기준합니다 수를 넣어주세요.')
m_list=int_string_M.split(' ')
m_list=list(map(lambda x : int(x), m_list))
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
m_list.sort()
for i in range(len(n_list)):
    find_num=int(n_list[i]) #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
        if int(m_list[mid]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[left]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[right]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif  int(m_list[mid]) > find_num :
            right=mid-1
        elif int(m_list[mid]) < find_num :
            left=mid+1

#각 숫자별 cnt 리스트 생성
#total_list=list(dict_num.values())
#리스트 요소들을 join하기 위해 문자열로 변환
total_list1=list(map(lambda x: str(x), list(dict_num.values())))
#문자열 공백으로 띄우고 합침
" ".join(total_list1)

#7차
N=int(input('보유하고 있는 카드의 수'))
n_list=list(map(lambda x : int(x), input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
M=int(input('비교할 기준이 되는 카드의 수'))
m_list=list(map(lambda x : int(x), input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
m_list.sort()

for i in range(len(n_list)):
#    find_num=n_list[i] #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        #mid=(left+right)//2 #중앙값의 인덱스
        if int(m_list[(left+right)//2]) == n_list[i]:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
            dict_num[str(n_list[i])]+=1  #값을 찾았으므로 해당키의 값을 +1
            print(n_list[i], m_list[(left+right)//2])
            break
        elif int(m_list[left]) == n_list[i]:   #내가 보유한 수가 left값인지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[right]) == n_list[i]:   #내가 보유한 수가 right값인지 확인
            dict_num[str(n_list[i])]+=1
            break
        elif int(m_list[(left+right)//2]) > n_list[i] : #찾고자 하는 값이 중앙값보다 작을 경우
            right=mid-1   #우측 시작범위를 줄임
            print(n_list[i], m_list[(left+right)//2])
        elif int(m_list[(left+right)//2]) < n_list[i] : #찾고자하는 값이 중앙값보다 클 경우
            left=mid+1    #좌측 시작범위를 줄임
            print(n_list[i],m_list[(left+right)//2])

total_list1=list(map(lambda x: str(x), list(dict_num.values())))
print(" ".join(total_list1))

#8차

#9차 시간초과 

#시간을 재보기로 함
import math 
import time 
start = time.time()
# 1 <<< list(map(lambda x : int(x), input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
# 2 <<< list(map(int, input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
end = time.time()
print(f"{end - start:.5f} sec")
#1 105.65195 sec
#2 13.92753 sec
# >> lambda쓰면 느려짐

N=int(input('보유하고 있는 카드의 수'))
n_list=list(map(int, input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
M=int(input('비교할 기준이 되는 카드의 수'))
m_list=list(map(int, input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0
m_list.sort()

for i in range(len(n_list)):
    find_num=n_list[i] #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while (left<=right): #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
        try:
            if int(m_list[mid]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
                dict_num[str(n_list[i])]+=1
                break
            elif int(m_list[mid]) > find_num :
                right=mid-1
            elif int(m_list[mid]) < find_num :
                left=mid+1
        except:
            #찾고자 하는 수가 left혹은 right일 때
            if int(m_list[left]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
                dict_num[str(n_list[i])]+=1
                break
            elif int(m_list[right]) == find_num:   #내가 보유한 수가 비교할 리스트에 존재하는지 확인
                dict_num[str(n_list[i])]+=1
                break

total_list1=list(map(str, list(dict_num.values())))
print(" ".join(total_list1))

##############################################################
#10차
N=int(input('보유하고 있는 카드의 수'))
#10
n_list=list(map(int, input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
#6 3 2 10 10 10 -10 -10 7 3
M=int(input('비교할 기준이 되는 카드의 수'))
#8
m_list=list(map(int, input('공백으로 수를 기준합니다 수를 넣어주세요.').split(' ')))
#10 9 -5 2 3 4 5 -10
dict_num = {}
for i in m_list:
    dict_num[str(i)]=0

m_list.sort()

find_num=n_list[i] #찾고자 하는 수(보유 카드)
#left = 0   #가장작은 수 인덱스
#right = len(m_list)-1 #가장 큰 수 인덱스
left, right = 0, len(m_list)-1
for i in range(len(n_list)):
    find_num=n_list[i] #찾고자 하는 수(보유 카드)
    left = 0   #가장작은 수 인덱스
    right = len(m_list)-1 #가장 큰 수 인덱스
    while left<=right: #비교할 수의 구간이 존재할 동안
        mid=(left+right)//2 #중앙값의 인덱스
        if int(m_list[mid]) == find_num:   #현재 서치값이 중앙값과 일치하다면
            dict_num[str(n_list[i])]+=1    #카운트
            break
        elif int(m_list[mid]) > find_num :
            right=mid-1
        elif int(m_list[mid]) < find_num :
            left=mid+1

total_list1=list(map(str, list(dict_num.values())))
print(" ".join(total_list1))

## 11차 시간초과

N=int(input())
#10
n_list=list(map(int, input().split(' ')))
#6 3 2 10 10 10 -10 -10 7 3
#6 3 2 10 10 10 -10 -10 7 3 3 3 3 3 
M=int(input())
#8
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10
#10 9 -5 2 3 4 5 -10 -10 -10 -10 -10
dict_num = {}


for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

#n_list=sorted(n_list[:N])           #이분 정렬을 위해 오름차순 정렬

#다른 사람 풀이 참조 수정
for n in range(len(n_list[:N])):
    if str(n_list[n]) not in dict_num: #만들어든 체크리스트에 현재의 탐색숫자가 없다면
        pass #0으로 나눈뒤에 pass
    else: #만들어둔 체크리스트에 탐색 숫자가 있다면 이분탐색
        #find_num=n_list[n] #찾고자 하는 수(보유 카드)
        left, right = 0, len(n_list[:N])-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                #dict_num[str(n_list[i])]+=1    #내방식대로 하면 모든 리스트를 돌아야 하기 때문에 비용이 늘어남
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                    left=mid+1

total_list1=list(map(str, list(dict_num.values())))
print(" ".join(total_list1))


#12차

N=int(input())
#10
n_list=list(map(int, input().split(' ')))
#6 3 2 10 10 10 -10 -10 7 3
#6 3 2 10 10 10 -10 -10 7 3 3 3 3 3 
M=int(input())
#8
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10
#10 9 -5 2 3 4 5 -10 -10 -10 -10 -10
dict_num = {}

for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

#n_list=sorted(n_list[:N])           #이분 정렬을 위해 오름차순 정렬

#다른 사람 풀이 참조 수정
for n in range(len(n_list[:N])):
    if str(n_list[n]) not in dict_num: #만들어든 체크리스트에 현재의 탐색숫자가 없다면
        pass #0으로 나눈뒤에 pass
    else: #만들어둔 체크리스트에 탐색 숫자가 있다면 이분탐색
        #find_num=n_list[n] #찾고자 하는 수(보유 카드)
        left, right = 0, len(n_list[:N])-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                #dict_num[str(n_list[i])]+=1    #내방식대로 하면 모든 리스트를 돌아야 하기 때문에 비용이 늘어남
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                    left=mid+1

print(' '.join([str(n) for n in dict_num.values()]))


#13차 
#시간복잡도 참고
#https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84

#리스트보다 딕셔너리가 시간복잡도가 훨씬 빠름
#sort나 sorted의 시간 복잡도는 O(NlogN) 

N=int(input())
#10
#여기서 문제 설명이 부족해서 혼동이 온듯함
#내가 가지고 있는 카드개수가 해당 숫자의 최대개수인 듯함
#내가 받은 카드 갯수만큼 입력한 리스트에서 끊어서 가져오는 형식이 아닌 모양
#이를 위해 for문 range에 [:N]으로 잡으면 이러면 매번 for문을 돌면서 시간복잡도가 늘어남 
"""
따라서 이 부분이 필요 없어지게 됨
n_list_len= len(n_list)
left_slice=n_list_len-N
#내가 입력한 숫자에서 내가 가진 카드 수 만큼 숫자를 가지기 위해 del
del n_list[-(left_slice):]
"""
#이분탐색을 하기위해 sorting
#sort()로 연산하면 값이 안들어감 따라서 sorted로 들어가야 함

n_list=sorted(list(map(int, input().split(' '))))
#12.20963 sec
#n_list=list(map(int, input().split(' ')))
#n_list.sort()
#13.42049 sec

#6 3 2 10 10 10 -10 -10 7 3
M=int(input())
#8
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10

dict_num = {}
for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

#다른 사람 풀이 참조 수정

#내가 가지고 있는 숫자들에 대해 각각 카운팅
for n in range(N): #내가가진 카드 요소 만큼 반복
    if str(n_list[n]) not in dict_num: #내가 찾고자 하는 숫자가 dict에 없다면 세지 않아도 되는 수이므로 
        print(n_list[n],'1')
        continue
    elif dict_num[str(n_list[n])] != 0: #만들어둔 체크리스트 딕셔너리에 0이외의 탐색 숫자가 있다면 이미 카운팅 한 것이므로 
        print(n_list[n],'2')
        continue
    elif dict_num[str(n_list[n])] == 0: #만들어든 체크리스트에 현재의 탐색숫자가 0이라면 (탐색해 보지 않은 것이므로) #이후에도 동일한 숫자가 나올 수 있긴 하지만
        print(n_list[n],'check')
        #이분탐색을 진행하기 위해 기준 수 초기화
        left, right = 0, N-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                left=mid+1        

dict_num 

print(' '.join([str(n) for n in dict_num.values()]))
#[str(dict_num[str(x)]) if str(x) in dict_num else '0' for x in m_list[:M]]
#print(' '.join(str(dict_num[str(x)]) if str(x) in dict_num else '0' for x in m_list[:M]))
#0.02601 sec
#print(' '.join([str(n) for n in dict_num.values()]))
#0.01500 sec


#14차

N=int(input())
#10
n_list=list(map(int, input().split(' ')))
#6 3 2 10 10 10 -10 -10 7 3 3 3 3 3

#n_list_len= len(n_list)
#left_slice=n_list_len-N
#내가 입력한 숫자에서 내가 가진 카드 수 만큼 숫자를 가지기 위해 del
if len(n_list)-N==0:
    pass
else:
    del n_list[-(len(n_list)-N):]
n_list.sort()

M=int(input())
#8
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10 10 10 10 10 10
if len(m_list)-M==0:
    pass
else:
    del m_list[-(len(m_list)-M):]


dict_num = {}
for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

for n in range(N): #내가가진 카드 요소 만큼 반복
    if str(n_list[n]) not in dict_num: #내가 찾고자 하는 숫자가 dict에 없다면 세지 않아도 되는 수이므로 
        continue
    elif dict_num[str(n_list[n])] != 0: #만들어둔 체크리스트 딕셔너리에 0이외의 탐색 숫자가 있다면 이미 카운팅 한 것이므로 
        continue
    elif dict_num[str(n_list[n])] == 0: #만들어든 체크리스트에 현재의 탐색숫자가 0이라면 (탐색해 보지 않은 것이므로) #이후에도 동일한 숫자가 나올 수 있긴 하지만
        left, right = 0, N-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                left=mid+1         

dict_num 
print(' '.join([str(n) for n in dict_num.values()]))


#final
#내가 보유한 숫자카드의 수
N=int(input())
#ex)10

#내가 가진 숫자카드의 수를 넘는 수가 입력될 수 있음
n_list=list(map(int, input().split(' ')))
#ex) 6 3 2 10 10 10 -10 -10 7 3 3 3 3 3

#내가 입력한 숫자에서 내가 가진 카드 수 만큼 숫자를 가지기 위해 del
#n_list_len= len(n_list)
#left_slice=n_list_len-N

#만약 보유카드수와 입력된 카드수가 동일할 경우
#굳이 이렇게 처리하는 이유는 카드수가 0일 때 아래의 코드로 실행하면 -0이 뜨면서 index 오류가 나기 때문
if len(n_list)-N==0:
    pass
#보유카드수와 입력된 숫자의 수가 다를 경우 보유카드 수 만큼 카드를 가짐
else:
    del n_list[-(len(n_list)-N):]
n_list.sort()

#내가 비교할 카드 수
M=int(input())
#ex)9
#비교할 수 입력
m_list=list(map(int, input().split(' ')))
#10 9 -5 2 3 4 5 -10 10 10 10 10 10

#위와 마찬가지로 비교할 카드수를 넘는 수가 입력될 수 있으므로 아래의 코드로 동일하게 처리
if len(m_list)-M==0:
    pass
else:
    del m_list[-(len(m_list)-M):]

#비교할 숫자에 대한 딕셔너리 생성
dict_num = {}
for i in m_list[:M]:    #받은 인자만큼의 길이까지 
    dict_num[str(i)]=0  #딕셔너리 생성

#탐색하는데 불필요한 작업을 최대한 배제하는 식으로 알고리즘 구성
for n in range(N): #내가가진 카드 요소 만큼 반복
    if str(n_list[n]) not in dict_num: #내가 찾고자 하는 숫자가 dict에 없다면 세지 않아도 되는 수이므로 
        continue
    elif dict_num[str(n_list[n])] != 0: #만들어둔 체크리스트 딕셔너리에 0이외의 탐색 숫자가 있다면 이미 카운팅 한 것이므로 
        continue
    elif dict_num[str(n_list[n])] == 0: #만들어든 체크리스트에 현재의 탐색숫자가 0이라면 (탐색해 보지 않은 것이므로) #이후에도 동일한 숫자가 나올 수 있긴 하지만
        left, right = 0, N-1
        while left<=right: #비교할 수의 구간이 존재할 동안
            mid=(left+right)//2 #중앙값의 인덱스
            if int(n_list[mid]) == n_list[n]:   #내가 보유한 수가 축소된 리스트 범위 내에 존재하는지 확인
                dict_num[str(n_list[n])]=n_list[left:right+1].count(n_list[n]) #이렇게 하면 범위가 제한된 상태에서 중복리스트들 모두 카운트하기 때문에 효율적
                break
            elif int(n_list[mid]) > n_list[n] :
                right=mid-1
            elif int(n_list[mid]) < n_list[n] :
                left=mid+1         

#M개의 숫자도 중복된 숫자가 있을 수 있음(간과해서 오래 걸린 부분)
#[str(dict_num[str(m)]) for m in m_list  if str(m) in dict_num]
print(' '.join([str(dict_num[str(m)]) for m in m_list  if str(m) in dict_num]))

#출력 시간측정

#print(' '.join(str(dict_num[str(x)]) if str(x) in dict_num else '0' for x in m_list[:M]))
#0.02601 sec
#print(' '.join([str(n) for n in dict_num.values()]))
#0.01500 sec

#sorting 시간측정 

#12.20963 sec
#n_list=list(map(int, input().split(' ')))
#n_list.sort()
#13.42049 sec