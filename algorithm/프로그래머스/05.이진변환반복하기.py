#https://school.programmers.co.kr/learn/courses/30/lessons/70129
s= "110010101001"	#[3,8]
s= "01110"	#[3,3]
s= "1111111"	#[4,1]

#최대 이진수 자릿수 뽑는 함수
def see_binary(N):
    if type(N)==int:
        n=N 
        now=1
        binary_l = []
        for j in range(N):
            if now>N:
                break
            else:
                now=now*2
                binary_l.append(0)
        for i,v in reversed(list(enumerate(binary_l))): #enumerate를 reversed하려면 list화 해야함
            #(2^i)라고 하면 2의 허수제곱으로 받아서 정수처리해서 0나옴
            #반드시 2^i로 쓰도록 하자
            print('n',n)
            if n - (2**i) >= 0:
                n = n - (2**i)
                binary_l[i]=1       
                print(binary_l, n)     
            else:
                binary_l[i]=0
        #단 지금 함수는 reverse해야 제대로된 이진수 표기가 됨.       
        #list(map(str,binary_l))[::-1]
        print(''.join(list(map(str,binary_l))[::-1]))
        return ''.join(list(map(str,binary_l))[::-1]) 
    if type(N)==str:
        now=0
        N=list(reversed(N))
        for j,v in enumerate(N): #enumerate는 reversed 불가
            now+=int(v)*2**j
        print('now',now)
        return see_binary(now)

def solution(s):
    #0제거한 string 초기화
    rm_zero=s
    #제거한 0의 수 초기화
    rmed_zero_len=0
    #제거한 0의 수 집계 초기화 
    tot_zero_len = 0
    #0제거한 횟수 초기화
    rm_zero_cnt = 0
    ing=True
    answer=[]
    while ing:
        if len([i for i in rm_zero if i==1]) == 1:
            ing=False #마지막 횟수와 0의 갯수를 세야하므로 여기서 break하면 안됨
        #0제거
        rm_zero = rm_zero.replace('0','')
        #제거한 0의 수
        rmed_zero_len = len(s)-len(rm_zero)
        #제거한 0의 수 합산
        tot_zero_len+=rmed_zero_len
        #0제거한 횟수 집계 
        rm_zero_cnt+=1
        #0제거한 string 길이 이진변환
        s=see_binary(len(rm_zero)) #input은 int
    answer=[rm_zero_cnt, tot_zero_len]
    return answer

####
def see_binary(N):
    if type(N)==int:
        n=N 
        now=1
        binary_l = []
        for j in range(N):
            if now>N:
                break
            else:
                now=now*2
                binary_l.append(0)
        for i,v in reversed(list(enumerate(binary_l))): 
            if n - (2**i) >= 0:
                n = n - (2**i)
                binary_l[i]=1       
            else:
                binary_l[i]=0
        return ''.join(list(map(str,binary_l))[::-1]) 
    if type(N)==str:
        now=0
        N=list(reversed(N))
        for j,v in enumerate(N): 
            now+=int(v)*2**j
        return see_binary(now)

def solution(s):
    rm_zero=s
    rmed_zero_len=0
    tot_zero_len = 0
    rm_zero_cnt = 0
    ing=True
    answer=[]
    while ing:
        if len([i for i in s if i=='1']) == 1:
            ing=False
        rm_zero = s.replace('0','')
        rmed_zero_len = len(s)-len(rm_zero)
        tot_zero_len+=rmed_zero_len
        rm_zero_cnt+=1
        s=see_binary(len(rm_zero)) 
        print('rm_zero1',rm_zero, 's', s)
        print(rm_zero_cnt, tot_zero_len)
    answer= [rm_zero_cnt, tot_zero_len]
    return answer

solution(s)

#다른 사람의 풀이
#bin()함수로 이진수 변환가능 단 이진수는 2:부터
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]