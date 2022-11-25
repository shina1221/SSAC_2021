#https://school.programmers.co.kr/learn/courses/30/lessons/68645

#풀이 https://developnote.tistory.com/26

answer = [[0 for j in range(1,i+1)] for i in range(1,n+1)]
x,y = -1, 0 #처음 시작은 아래로 내려가기 때문에 x=-1
num=1

for i in range(n): #방향
    for j in range(i, n): #좌표구하기
        if i %3 ==0: #아래로
            x+=1
        elif i %3 ==1: #우측방향으로
            y +=1
        else: #위로
            x -= 1
            y -= 1
        answer[x][y] =num
        num+=1

sum(answer, []) #이렇게 합칠 수도 있음 


#개인 실패
n=4
nxt_n=4

tot=[[-1]*i for i in range(1, n+1)]
cnt = 0
chk_i=[0]
tail_chk=0

for i in reversed(range(n)):
    if chk_i
    chk_i.append(chk_i+2)
    #i기준 행기준
    now=chk_i.pop(0)
    #맨아랫줄을 안채웠다면
    if tail_chk != 1:
        r_i = range(i) 
    #맨아랫줄을 이미 채웠다면
    #거꾸로 행을 올라가며 채워야 하므로 reverse
    if tail_chk ==1:
        r_i = reversed(range(i-1)) #
    for j in r_i:
        if tail_chk==1:
            tot[j][-1]=cnt=1
        else:    
            #아래방향으로 채우기
            tot[i][now]=cnt+1
            #만약 맨 아래행까지 도달했다면
            if i==nxt_n-1:
                #그 다음 맨 마지막 행 표시
                nxt_n-=1
                #우측방향으로 채움
                tot[i][j]=cnt+1
                #우측방향의 맨 마지막에 도달한다면 위로 올라가야함
                if tot[i][i]!=-1:
                    tail_chk=1
    tail_chk=0


print(tot)
             


import numpy as np

tot=[np.array([-1])*i for i in range(1, n+1)]
tot=np.array(tot)
chk_bottom=0
chk_tail=0
cnt=0
n=6
last_i=-1
#np.where(arr_tot==-1)[0][0]
#np.where(arr_tot==-1)[1][0]
now=list(range(n/2))
for i in reversed(range(n)):
    #값이 채워지지 않은 값중 가장 가까운 좌표
    index_i, index_j= np.where(tot==-1)[0][0],np.where(tot==-1)[1][0]
    if chk_bottom==1 and chk_tail==1:
        i_r = reversed(range(i))
        nnow=now.pop(0)
    if chk_bottom==1 and chk_tail!=1:
        i_r = range(i)
        nnow=now.pop(0)
    else:
        i_r = range(i)
    for j in i_r:
        if chk_bottom!=1 and chk_tail!=1:
            print('1', i,j)
            if i==j:
                last_i = i
                chk_bottom=1 
            tot[i][nnow]=cnt+1
            break
        elif chk_bottom==1 and chk_tail==0:
            print('2', i,j)
            if tot[last_i][j]==-1:
                tot[last_i][j]=cnt+1
                if i==j:
                    chk_tail=1
        if chk_bottom==1 and chk_tail==1:
            print('3', i,j)
            tot[index_i][index_j]= cnt+1
    print(tot)
            #if i==index_i and j == index_j:

        


    

        






    
