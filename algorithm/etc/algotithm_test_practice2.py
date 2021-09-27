#문자열 다루기 기본
#1차 실패(일부만 성공)
def solution(s):
    answer=0
    try:
        if len(s)==4 or len(s)==6:
            int(s)
            answer = True
        else:
            pass
    except:
        answer = False
    return answer
        
#2차 성공
def solution(s):
    if len(s)==4 or len(s)==6:
        answer=True
        try:
            int(s)
        except:
            answer=False
    else:
        answer=False
    return answer

#정수 내림차순으로 배치하기
def solution(n):
    #리스트로 만들기 위해선 요소가 str이어야 함
    n=list(map(lambda x: int(x), list(str(n))))
    for k in range(len(n)):
        for j in range(len(n)-(k+1)):  #점점 비교할 대상이 줄어듦 
            #print('k:',k,n[k],'j:',j,n[j])
            if n[k] < n[k+j+1]:
                max_i = n[k+j+1]
                n[k+j+1] = n[k]
                n[k] = max_i
    #n=list(map(lambda x: str(x), n))
    answer = int(''.join(list(map(lambda x: str(x), n))))
    return answer
    
#자연수 뒤집어 배열로 만들기
def solution(n):
    n=list(str(n))
    n.reverse()
    answer=list(map(lambda x : int(x), n))
    #answer = ''.join(n)
    return answer

#핸드폰 번호 가리기
def solution(phone_number):
    p=list(phone_number)
    for pp in range(len(p[:-4])):
        p[pp]='*'
    answer = ''.join(p)
    return answer

#K번째수
array =  [1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#Return=[5, 6, 3]


def solution(array, commands):
    #리스트를 안 만들어주고 공백 리스트로 시작하면 Nonetype 에러 뜸
    answer=list(range(0,len(commands)))
    print(answer)
    for com_i in range(len(commands)):
        #print(commands[com_i][0])
        #print(commands[com_i][1])
        #print(array[commands[com_i][0]-1:commands[com_i][1]])
        find_list = array[commands[com_i][0]-1:commands[com_i][1]]
        find_list.sort()
        #print('find_list:',find_list)
        find_index=commands[com_i][-1]-1
        #print('find_index:' find_index)
        find_num=find_list[find_index]
        #print('find_num:', find_num)
        answer[com_i]= find_num
    return answer

#하샤드 수
def solution(arr):
    arr_after= list(map(lambda x: int(x),list(str(arr))))
    sum_arr=sum(arr_after)
    #print(sum_arr)
    if arr%sum_arr ==0:
        answer=True
    else:
        answer=False
    return answer

#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer=[]
    ing_l = [x for x in arr if x/divisor==int(x/divisor)]
    #print(ing_l)
    if len(ing_l)==0:
        answer=[-1]
    else:
        ing_l.sort()
        answer=ing_l
    return answer

#모의고사 //1일
def solution(answers):
    #First
    def find_first_now(i):
        first_now=0
        if i % 5 !=0:
            first_now=i%5
        else:
            first_now=5
        return first_now
    first_cnt=0
    #Second
    def find_second_now(j):
        second_now=0
        #8로 나눠 홀수 번째 수들이 모두 2
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
    #Third
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
    for i in range(len(answers)):
        #첫번째 수는 i+1로 시작
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
    print(total_dict)
    #이름 바꾸기
    answer=[int(k) for k, v in total_dict.items() if v == max(total_dict.values())]
    answer.sort()
    return answer

#완주하지 못한 선수
#1차 안됨
def solution(participant, completion):
    memo_l=[] #미완주자 리스트
    non_l=[] #미완주자 리스트
    for i in participant:
        #동명이인 완주자 검출
        #이전에 동명이인을 완주한 사람으로 검출했다면 미완주자로 간주
        if i in memo_l:
            non_l.append(i)
            continue
        #완주자 검출
        elif i in completion:
            memo_l.append(i)
        #동명이인이 아닌 미완주자 검출
        else:
            non_l.append(i)
    answer=non_l[0]
    return answer

#2차 안됨
def solution(participant, completion):
    answer=''
    for i in participant:
        if participant.count(i)>=2:
            answer=i
            break
        if i not in completion:
            answer=i
    return answer

#3차 성공 // 2시간 걸림
def solution(participant, completion):
    answer=''
    participant.sort()
    completion.sort()
    lp= len(participant)
    lc= len(completion)
    if lp>=lc:
        completion.append(0)
        range_i =lp
    else:
        participant.append(0)
        range_i =lc
    answer = [participant[i] for i in range(range_i) if participant[i] != completion[i]][0]
    return answer    


#2016년
from datetime import date
def solution(a,b):
    week = ['MON', 'TUE', 'WED','THU','FRI','SAT','SUN'] 
    answer=week[date(2016, int(a), int(b)).weekday()]
    return answer

#소수찾기
#1차 실패 //시간초과
def solution(n):
    dict_i = {}
    cnt=0
    for i in range(1, n+1):
        dict_i[str(i)] = []
        for j in range(1,n+1):
            if i%j==0:
                #print(i,j)
                dict_i[str(i)].append(j)
    #print(dict_i)
    for k in dict_i:
        if len(dict_i[k]) ==2:
            cnt+=1 
    answer= cnt
    return answer
                
#2차    
def solution(n):
    answer=0
    dict_i={}
    for i in range(2, n+1):
        #dict_i[str(i)] = {}
        if i in dict_i:
            answer+=1
            continue
        #else:
        #    for j in range(1, i+1):
        #        if i%j==0 and :
        #            dict_i[str(i)]=j
        #        print(dict_i)
        elif len([j for j in range(1, i+1) if i%j==0]) == 2:
            dict_i[str(i)] = {}
            #print([j for j in range(1, i+1) if i%j==0])
            dict_i[str(i)]=1 #([j for j in range(1, i+1) if i%j==0][-1])
            answer+=1
    print(dict_i)
    print(sum(dict_i.values()))
    return answer

#3차 11번, 효율 문제                
def solution(numbers):
    answer=0
    memo_dict={}
    for i in range(1,numbers+1):
        for j in range(1,numbers+1): 
            if i*j > numbers:
                break
            else:
                try: 
                    memo_dict[str(i*j)].append([i,j])
                except:
                    memo_dict[str(i*j)] = []
    for dd in memo_dict.values():
        if len(dd)==1:
            #print(dd)
            answer+=1
    return answer

#4차 [질문 참조]
#에라토스테네스의 체 알고리즘 //2시간
""""
출처:한빛미디어
1) 2부터 N까지의 모든 자연수 나열
2) 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
  //이떄 i값은 소수. 즉 지워지지 않은 소수중에 가장 작은 수
3) 남은 수 중에서 i의 배수를 모두 제거
  //단 i는 제거하지 않음
4) 더 이상 반복할 수 없을 때까지 2번과 3번의 과정 반복
"""
#설명참고하고 수정 및 작성        

def solution(n):
    import math
    prime_number=[]
    array_i = [True for i in range(n+1)] #내가 생각하지 못한 부분
    #에라토스테네스의 체 알고리즘 수행
    #2부터 n의 제곱근까지의 모든 수를 확인하며 ###POINT 제곱근####
    #소수점을 floor 내림으로 처리
    for i in range(2, (math.floor(n**0.5))+1):  ####POINT#####
        if array_i[i] == True:  #i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        # j는 배수값
            j=2
            try:
                while i*j <= n:        
                    #print('i',i, 'j', j)
                    array_i[i*j] =False
                    j +=1
            except:
                array_i[i*j] =False
                break
    #print(array_i)
    #모든 소수 출력
    for i in range(2, n+1):
        #i가 참(True)인경우(소수인경우) append
        if array_i[i]:
            prime_number.append(i)     
    #print(prime_number)       
    return len(prime_number)    

#clean_ver    
def solution(n):
    import math
    prime_number=[]
    array_i = [True for i in range(n+1)]
    numm = math.floor(n**0.5) + 1
    print(numm, type(numm))
    #소수점을 floor 내림으로 처리
    for i in range(2, (math.floor(n**0.5))+1):
        if array_i[i] == True: 
            j=2
            try:
                while i*j <= n:        
                    print('i',i, 'j', j)
                    array_i[i*j] =False
                    j +=1
            except:
                array_i[i*j] =False
                break
    print(array_i)
    for i in range(2, n+1):
        if array_i[i]:
            prime_number.append(i)
    print(prime_number)

            
#예산//2일
#1차
def solution(d, budget):
    #경우의 수를 볼 숫자의 개수
    d.sort()
    cnt=0
    result={}
    memo_d ={}
    summ=0
    for dd in range(len(d)):
        #n(cnt)개 별 경우의 수
        #memo_d[str(cnt+1)]=d[dd:dd+cnt]
        memo_d[str(cnt+1)]= [] #([d[dd]])
        result[str(cnt+1)]=0
        #print(memo_d)
        #for ll in range(int(d.index(dd)+cnt), len(d)):
        letf_start_num =dd+cnt
        print(dd)
        summ+=d[dd]
        print(summ)
        for ll in range(letf_start_num, len(d)):
            #memo_d[str(cnt)].extend([d[ll]])
            # 살려 memo_d[str(cnt)].append([d[dd],d[ll]])
            total_sum=sum([d[dd],d[ll]])
            summ+=d[ll]
            print(summ)
            if total_sum+d[ll] <= budget:
                result[str(cnt+1)]=1
            else:
                continue
            #부서 수 증가
            cnt+=1
            solution(d[left_start_num+1:len(d)])
        #memo_d. dd+ll
        print(memo_d)

#2차 3,21,23번에서 걸림
def solution(d,budget):
    d.sort()
    result=0
    cnt=0
    while result<=budget and cnt<len(d):
        result+=d[cnt]
        cnt+=1
    print(result)
    return cnt

#3차 중간에 시간초과 있어서 실패
def solution(d,budget):
    import itertools
    result=0
    for dd in range(len(d),0,-1):
        if result > 0:
            break
        else: 
            #각 요소가 튜플로 나옴
            now_l=list(itertools.combinations(d, dd))
            now_l.sort()
            now_l[::-1]
            for j in now_l:
                #print(j)
                j=list(j)
                if result > 0:
                    break
                elif sum(j) <= budget:
                    result =len(j)
                    break
    return result

#N차 성공
import itertools
def solution(d, budget): #조합 출력
    for dd in range(len(d),1,-1):
        now_l=list(itertools.combinations(d, dd)
        for j in range(len(now_l)):
            if sum(j) <= budget:
            break
    return len(list(itertools.combinations(d, dd))

#체육복
#1차 실패
def solution(n,lost, reserve):
    cnt=0
    inven=[]
    answer=len(reserve)
    #양쪽 리스트에 같은 수가 존재하면
    for lost_i in range(len(lost)):
        #빌려줄 사람이 도둑맞았으면 못빌려줌
        if lost[lost_i] in reserve:
            #하지만 본인몫은 챙김
            #삭 cnt+=1
            #삭 lost.remove(lost_i)
            reserve.remove(lost[lost_i])
            lost[lost_i]=-2
    #유효한 값만 남기기 위해 정수인 것만 남겨둠
    #참고 left_l=len([i for i in lost if i>0])
    #print([i for i in lost if i>0])
    #삭 Eanswer=n-len([i for i in lost if i>0])
    for re_i in reserve:
        #범위 체크
        inven.append([re_i-1, re_i+1])
    #print(inven)
    for li in [i for i in lost if i>0]:
        for inven_i in range(len(inven)):
            #범위 0이 있어도 그냥 무시해도 됨 lost에 들어올 숫자가 아님
            if li in inven[inven_i]:
                #구제된 사람
                cnt+=1
                #lost.remove(li)
                #빌려준 몫 삭제
                #단 단 리스트 숫자가 for문을 도는데 변하면 안되니 값 변경
                inven[inven_i]=[-1]
                break
            #print('cnt:', cnt)
        #print('lost:',lost)
    #최종적으로 빌려주지도 않은 사람들이 inven에 남음
    left_p=len([i for i in inven if i!=[-1]])
    #print('left_p', left_p)
    answer= answer + cnt +left_p
    return answer

#2차 성공
def solution(n,lost, reserve):
    ### 밑의 두줄은 질문 참조
    lost.sort()
    reserve.sort()
    ###
    cnt=0
    inven=[]
    #체육복을 가지고 있는 사람 확보
    answer_mid=n-len(lost)
    for lost_i in range(len(lost)):
        if lost[lost_i] in reserve:
            reserve.remove(lost[lost_i])
            lost[lost_i]=-2
            cnt+=1
    for re_i in reserve:
        #범위 체크
        inven.append([re_i-1, re_i+1])
    check_lost=[i for i in lost if i>0]
    for inven_i in range(len(inven)):
        for li in range(len(check_lost)):
            if check_lost[li] in inven[inven_i]:
                cnt+=1
                inven[inven_i]=[-1]
                check_lost[li]=-2
                break
        print(inven)
        print(check_lost)
        print(cnt)
    answer= answer_mid + cnt 
    return answer

#시저암호 //2일 걸림

def solution(s,n):
    s=list(s)
    #26개
    alphabet_l =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    new_list=[]
    now_num=0    
    for ss in s:
        #ss가 공백이면
        if ss == ' ':
            new_list.append(' ')
            continue
        #알파벳인지 특수기호인지 확인 
        #이렇게 했다가 연산 우선순위 때문에 오류남
        #elif ss.lower() in alphabet_l ==True:
        #알파벳이면
        elif (ss.lower() in alphabet_l)==True:
            #ss가 대문자면
            if ss.isupper() == True:  
                ss= ss.lower()
                now_num = alphabet_l.index(ss)
                #print(ss, now_num)
                #기존의 알파멧 갯수를 넘는다면
                if (now_num + n) > 25:
                    #1번째는 0부터 시작하므로 -1추가
                    #대문자로 변경해주고 append
                    new_list.append(alphabet_l[(now_num + n)-25-1].upper())
                else:
                    new_list.append(alphabet_l[now_num+n].upper())
                #print('ss1:',ss)
            #ss가 소문자라면
            elif ss.islower() == True:
                now_num = alphabet_l.index(ss)     
                #기존의 알파멧 갯수를 넘는다면
                if now_num + n > 25:
                    new_list.append(alphabet_l[(now_num + n)-25-1])  
                else:
                    new_list.append(alphabet_l[now_num+n])
                #print('ss2:',ss)
        #ss가 특수기호라면
        else:
            new_list.append(ss)
    return ''.join(new_list)

#비밀지도//3시간 걸림
def solution(n, arr1, arr2):
    #변수의 자리를 만들어주고 시작
    #왜냐하면 실제 이진수를 구하고 채우지 못한 자리가 있을 수 있기 때문
    #같은 for문 내에서 만들었다가 둘이 연동되서 에러남 반드시 따로 할 것
    total_arr1=[]
    for k in range(n):
        mini_list1=[]
        for j in range(n):
            mini_list1.append('')
        total_arr1.append(mini_list1)
    total_arr2=[]
    for kk in range(n):
        mini_list2=[]
        for jj in range(n):
            mini_list2.append('')
        total_arr2.append(mini_list2)
    for n1_num in range(len(arr1)):
        n1=arr1[n1_num]
        #세부 리스트로 들어가기 위한 숫자 
        cnt1=0
        if n1 == 0:
            #이미 만들어 뒀으므로 패스
            continue
        if n1 == 1:
            total_arr1[n1_num] = (['','','','', '#'])
            continue
        else:
            #세부리스트 맨 마지막에서 시작
            while n1 >=1: 
                #몫
                cnt1-=1
                quo1=n1//2
                #나머지
                rem1=n1%2 * '#'
                n1=quo1
                total_arr1[n1_num][cnt1]=rem1
    #print(total_arr1)
    for n2_num in range(len(arr2)):
        n2=arr2[n2_num]
        #세부 리스트로 들어가기 위한 숫자 
        cnt2=0
        if n2 == 0:
            #이미 만들어 뒀으므로 패스
            continue
        if n2 == 1:
            total_arr2[n2_num] = (['','','','', '#'])
            continue
        else:
            #세부리스트 맨 마지막에서 시작
            while n2 >=1: 
                #몫
                cnt2-=1
                quo2=n2//2
                #나머지
                rem2=n2%2 * '#'
                n2=quo2
                total_arr2[n2_num][cnt2]=rem2        
    #print(total_arr2)
    answer=[]
    for ijk in range(n):
        last_arr=[]
        for ij in range(n):
            if total_arr1[ijk][ij] =='' and total_arr2[ijk][ij]=='':
                last_arr.append(' ')
            else:
                last_arr.append('#')
        #print(last_arr)
        answer.append(''.join(last_arr))
    return answer









