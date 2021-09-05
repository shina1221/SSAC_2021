def solution(numbers):
    import math
    answer=0
    #문자열을 리스트로 반환
    numbers_list=list(numbers)
    #num_list=list(map(lambda x: int(x), list(numbers)))
    #조합생성
    from itertools import permutations
    total_list=[]
    for i in range(len(numbers_list)):
        #total_list.extend(list(permutations(cnt_list, i+1)))
        total_list.extend(permutations(numbers_list, i+1))
    #int로 변경하기 위해 튜플형태의 데이터를 리스트로 변경
    total_list1=list(map(lambda x: list(x), total_list))
    #각 리스트 별 요소들 join
    #[''.join(x) for x in total_list1]
    #각 리스트별 요소들 int화 
    #[int(x) for x in [''.join(x) for x in total_list1]]
    #중복 수를 제거하여 조합으로 나온 숫자리스트 산출
    total_int=list(set([int(x) for x in [''.join(x) for x in total_list1]]))
    #소수찾기
    total_int1=len(total_int)*[True]
    answer=0
    for i in range(len(total_int)):  
        if total_int[i]==1 or total_int[i]==0:            #소수인지 확인하려는 숫자가 0이나 1이면 
            total_int1[i]=False        #0이나 1은 소수가 아니므로
            continue                   #넘어감
        cnt=0         #소수의 개수를 세기위해 0으로 초기화       
        for j in range(1, math.floor(total_int[i]**0.5)+1): #소수인지 확인하고자 하는 기준수의 루트값 만큼 반복
            print(total_int[i],j)
            if total_int[i]%j==0: #약수 갯수 구하기
                cnt+=1
            if cnt > 1: #소수가 아닐 때  (소수이면 1만 검출)
                total_int1[i]=False
                break
    answer=sum(total_int1) #소수인 조합의 개수 산출
    return answer




