
#직사각형 별찍기############################ 안됨
#strip()메서드를 사용하여 Python의 문자열에서 따옴표 제거
#1차 시도  #기댓값과 완전 똑같이 해도 안됨
def square_star(n,m):
    jj = n*"*"
    new_l = []
    for i in range(m):
        new_l.append(jj)
        new_l.append("\n")
    result_new_l="".join(new_l)
    result_new_l= str(result_new_l)
    return print(result_new_l)
#    return print('"'+result_new_l+'"') #기댓값 똑같

square_star(5,3)


####

#나누어 떨어지는 숫자 배열
arr= [5, 9, 7, 10]
divisor =5

arr=[2, 36, 1, 3]
divisor=1

arr=[3,2,6]
divisor=10



#모의고사###다시
#뒷자리 기준
    def find_first_now(i):
        first_now=0
        if i % 5 !=0:
            first_now=i%5
        else:
            first_now=5
        return first_now
    #first_cnt=0
    for i in range(len(answers)):
        print(find_first_now(i+1))
        #첫번째 수는 i+1로 시작
        if answers[i]==find_first_now(i+1):
            first_cnt+=1
    #print(first_cnt)

answers=[1,3,2,4,2]

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
    #max_cnt=max([first_cnt,second_cnt,third_cnt])
    #이름 바꾸기
    answer=[int(k) for k, v in total_dict.items() if v == max(total_dict.values())]
    answer.sort()
    return answer


answers=[1,3,2,4,2]
solution(answers)

#가장 높은 점수 찾기
    print(first_cnt)
    print(second_cnt)
    print(third_cnt)
    max_cnt=max([first_cnt,second_cnt,third_cnt])
    result=[x for x in [first_cnt,second_cnt,third_cnt] if x == max([first_cnt,second_cnt,third_cnt])]
    return result












for i in [5,6,9,8,4,2,30]:    
    def find_third_now(i):
        third_now=0
        #끝자리수 기준으로 숫자 나뉨
        if i%10==1 or i%10==2:
            third_now=3
            print('1')
            #break
        if i%10==3 or i%10==4:
            third_now=1
            print('2')
            #break
        if i%10==5 or i%10==6:
            third_now=2
            print('3')
            #break
        if i%10==7 or i%10==8:
            third_now=4
            print('4')
            #break
        if i%10==9 or i%10==10:
            third_now=5
            print('5')
        return third_now
    find_third_now(i)
    print('=====')

        return first_now
    first_cnt=0

    
    second_cnt=0
    for i in range(len(answers)):
        second_now=i%8
    
    third_cnt=0
            
    for i in range(len(answers)):    

        print(first_now, second_now, third_now)
        elif answers[i]==first_now:
            first_cnt+=1
        elif answers[i]==second_now:
            second_cnt+=1
        elif answers[i]==second_now:
            third_cnt+=1
        print(first_now)
        print(second_now)
        print(third_now)        
    #가장 높은 점수 찾기
    print(first_cnt)
    print(second_cnt)
    print(third_cnt)
    max_cnt=max([first_cnt,second_cnt,third_cnt])
    result=[x for x in [first_cnt,second_cnt,third_cnt] if x == max([first_cnt,second_cnt,third_cnt])]
    return result

    #중복 출력
    #sorting
answers=[1,2,3,4,5]
solution(answers)

answers=[1,3,2,4,2]
solution(answers)


        elif i >= 5:
            first_now=i%5 
   

from iteration_utils import duplicates

listNums = [1,1,2,3,3,4,5,5,5,5,6,8,8]

def listDups(listNums):
  return list(duplicates(listNums))





for i in range(len(answers)):
    if (i < 5 and i%5 == 1) or (i >=5 and i%5 == 1):
        print('1', i)
    elif  (i < 5 and i%5 == 2) or (i >=5 and i%5 == 2):    
        print('2',i)
        

    first_num = math.ceil(len(answers)/5)
    second_num = math.ceil(len(answers)/8)

    first_l = list(range(1,6)) * first_num
    #뒷자리 숫자가 끝나는 것에 따라 1-5가 정해짐

    second_l = [2,1,2,3,2,4,2,5] * second_num  










#1번 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 =[1:6]
def solution(answers):
    #올림
    rep1=celi(len(answer)/5)
    #첫번째 수포자
    my_answer1=list(range(1,6))*rep1
    #두번째 수포자
    #2번 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5 =(2,[1:6])
    [for ]
    rep1=celi(len(answer)/2)
    my_test_2=0
    my_test_2_cnt=0
    while len(my_test)<len(answer):
        #수포자의 답안 작성
        my_test_2+=1
        for i in [1,3,4,5]:
            if my_test_2%2!=0:
                if i==answer[my_test_2]:
                    my_test_2_cnt+=1
                    #continue
            else:
                2==answer[my_test_2]
                my_test_2_cnt+=1





#소수찾기

def solution(n):
    answer=0
    memo_l=[]
    for i in range(2, n+1):
        #print(i)
        #print([j for j in range(1, i+1) if i%j==0])        
        if [j for j in range(memo_l[-1]+1, i+1) if i%j==0][1] == i:
            print(j)
            answer+=1
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

dict_i ={'2': 1, '3': 1, '4': {}, '5': 1, '6': {}, '7': 1, '8': {}, '9': {}, '10': {}}
###3차
def solution(n):
    answer=0
    dict_i={}
    for i in range(n+1, 2, -1):
        dict_i[str(i)] = {}
        if i in dict_i:
            answer+=1
            continue
        #elif len([j for j in range(1, i+1) if i%j==0]) == 2:
        else:
            for j in range(1, i+1):
                comp=[1,i]
                if i%j == 0 and i not in comp==True:
                    continue
                    


            dict_i[str(i)]=1
            





        #이전에 검출했던 숫자 리스트 포함 여부에 따라 리스트 갱신
        elif [j for j in range(memo_l[-1]+1, i+1) if i%j==0][1] == i:
            memo_l.append(i)
            answer+=1
        else:
            pass




solution(4)
#1과 자기자신i뿐 list[1]=i

        print([j for j in range(1, i+1) if i%j==0])
        

        if [i,j for i in range(1, n+1)for j in range(1, i+1) if i%j==0][1] == i:
            answer+=1
            #dict_i[str(i)]=j
    dict_i
            
            answer+=1     
    return answer        

#[i j for i in range(1, n+1)for j in range(1, i+1) if i%j==0][1]
        

dddd=[(1, 3, 2), (1, 3, 5), (1, 3, 4), (1, 2, 5), (1, 2, 4), (1, 5, 4), (3, 2, 5), (3, 2, 4), (3, 5, 4), (2, 5, 4)]
#예산
#중간에 시간초과 있어서 실패

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
#2차
def solution(d,budget):
    import itertools
    result=0
    for dd in range(1,len(d)+1):
        if result > 0:
            break
        else: 
            #각 요소가 튜플로 나옴
            now_l=list(itertools.combinations(d, dd))
            now_l.sort()
            #print(list(map(lambda x : len(x) if sum(x) >=9 else '', now_l)))
            for j in now_l:
                #print(j)
                j=list(j)
                if result > 0:
                    break
                while sum(j) <= budget:
                    #이전거로 뽑아야 하는데
                    result =len(j)
                    break
    return result
    
d= [1,3,2,5,4] 
budget=9
solution(d,budget)

d=[2,2,3,3]
budget=10
solution(d,budget)



print(result)
len(result)
#len(list(itertools.combinations(d, dd)))
return len(list(itertools.combinations(d, dd))  



import itertools
def solution(d, budget): #조합 출력
    for dd in range(len(d),1,-1):
        now_l=list(itertools.combinations(d, dd)
        for j in range(len(now_l)):
            if sum(j) <= budget:
            break
    return len(list(itertools.combinations(d, dd))  

#d[5:0:-1]  
d=[1,3,2,5,4]
budget =9
solution(d,budget)

d= [2,2,3,3] 
budget=10
solution(d,budget)

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

solution(d,budget)

        cnt+=1
        #print(memo_d)

    answer = 0
    return answer

def combinations(self): # n=5, r=2 resultList = list(itertools.combinations(["1", "2", "3", "4", "5"], 2)) print("경우의 수 : {}개".format(len(resultList))) print(*resultList, sep="\n")




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

n=5
lost = [2,4,5]
reserve=[1,3,5]
solution(n,lost, reserve)

n=5
lost = [2,4]
reserve=[1,3,5]
solution(n,lost, reserve)

n=5
lost = [2,4]
reserve=[3]
solution(n,lost, reserve)

n=3
lost = [3]
reserve=[1]
solution(n,lost, reserve)

    for li in lost:
        for inven_i in inven:
            #범위 0이 있어도 그냥 무시해도 됨 lost에 들어올 숫자가 아님
            if li in inven_i:
                #구제된 사람
                cnt+=1
                lost.remove(li)
                #빌려준 몫 삭제
                inven.remove(inven_i)
            break






#시저암호

def solution(s,n):
    s=list(s)
    #26개
    alphabet_l =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u''v','w','x','y','z']    
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
        elif ('A'.lower() in alphabet_l)==True:
            #ss가 대문자이면
            if ss.isupper() == True:  
                #서치하기 위해 소문자로 변경
                ss= ss.lower()
                now_num = alphabet_l.index(ss)
                #index번호 + n이 25를 넘는다면(=기존의 알파벳 갯수를 넘는다면//26개지만 파이썬은 0부터 시작하므로) 
                if now_num + n > 25:
                    now_num=alphabet_l[((now_num + n)-25)]
                    new_list.append(alphabet_l[now_num].upper())
                    #continue    
                    #다시 대문자로 변경해서 append
                    #인덱스 번호가 25 이하라면
                    else:
                    new_list.append(alphabet_l[now_num+n].upper())
                    #continue
                    print('ss1:',ss)
                #ss가 소문자이면
            elif ss.islower == True:
                now_num = alphabet_l.index(ss)
                #인덱스 번호가 25 초과라면
                if now_num + n > 25:
                    now_num=alphabet_l[((now_num + n)-25)]
                    new_list.append(alphabet_l[now_num])
                    continue    
                #인덱스 번호가 25 이하라면
                else:
                    new_list.append(alphabet_l[now_num+n])
                    continue
                print('ss2:',ss)
            #new_list.append(alphabet_l[now_num+n])
        #알파벳도 아닌 특수문자라면
        else:
            new_list.append(ss)
            #continue    
            #최종결과물 출력
    return ''.join(new_list)

s=list('Hey Boy Z!') 
n=1
solution(s,n)

s=list('z') 
n=1
solution(s,n)

############

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

s=list('Hey Boy Z!') 
n=1
solution(s,n)


#비밀지도
#지도는 길이가 n인 정사각형 배열
#각 칸은 공백 또는 벽으로 이뤄짐
#리스트 만들어 둠

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

ing_list=[]
for jj in arr1: 
    while jj>=1: 
        quo=n//2
        rem=n%2
        n=quo
        ing_list.append(rem)
        print(n)    
for jj in arr2: 
    while jj>=1: 
        quo=n//2
        rem=n%2
        n=quo
        if 
        ing_list.append(rem)
        print(n)
######################################################3
#각 array별 이진수 뽑음
total_arr1=[]
#변수의 자리를 만들어주고 시작
#왜냐하면 실제 이진수를 구하고 채우지 못한 자리가 있을 수 있기 때문
for k in range(n):
    mini_list=[]
    for j in range(n):
        mini_list.append('')
    total_arr1.append(mini_list)

#total_arr2에도 리스트를 만들어 둠
total_arr2=total_arr1

for n1_num in range(len(arr1)):
    n1=arr1[n1_num]
    ing_list1=[]
    #세부 리스트로 들어가기 위한 숫자 
    cnt=0
    if n2 == 0:
        continue
    if n2 == 1:
        total_arr2[n2_num] = (['','','','', '#'])
        continue
    else:
        #세부리스트 맨 마지막에서 시작
        while n1 >=1: 
            #몫
            cnt-=1
            quo1=n1//2
            #나머지
            rem1=n1%2 * '#'
            n1=quo1
            total_arr1[n1_num][cnt]=rem1

#print(total_arr1)


for n2_num in range(len(arr2)):
    n2=arr2[n2_num]
    ing_list1=[]
    #세부 리스트로 들어가기 위한 숫자 
    cnt=0
    if n2 == 0:
        #이미 만들어 뒀으므로 패스
        continue
#    if n2 == 1:
#        total_arr2[n2_num] = (['','','','', '#'])
#        continue
    else:
        #세부리스트 맨 마지막에서 시작
        while n2 >=1: 
            #몫
            cnt-=1
            quo2=n2//2
            #나머지
            rem2=n2%2 * '#'
            n2=quo2
            total_arr1[n2_num][cnt]=rem2

print(totsal_arr2)
        

#################
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


n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
solution(n,arr1, arr2)

n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
solution(n,arr1, arr2)

def solution(n, arr1, arr2):
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
        cnt1=0
        if n1 == 0:
            continue
        if n1 == 1:
            total_arr1[n1_num] = (['','','','', '#'])
            continue
        else:
            while n1 >=1: 
                cnt1-=1
                quo1=n1//2
                rem1=n1%2 * '#'
                n1=quo1
                total_arr1[n1_num][cnt1]=rem1
    #print(total_arr1)
    for n2_num in range(len(arr2)):
        n2=arr2[n2_num]
        cnt2=0
        if n2 == 0:
            continue
        if n2 == 1:
            total_arr2[n2_num] = (['','','','', '#'])
            continue
        else:
            while n2 >=1: 
                #몫
                cnt2-=1
                quo2=n2//2
                rem2=n2%2 * '#'
                n2=quo2
                total_arr2[n2_num][cnt2]=rem2        
    answer=[]
    for ijk in range(n):
        last_arr=[]
        for ij in range(n):
            if total_arr1[ijk][ij] =='' and total_arr2[ijk][ij]=='':
                last_arr.append(' ')
            else:
                last_arr.append('#')
        answer.append(''.join(last_arr))
    return answer


