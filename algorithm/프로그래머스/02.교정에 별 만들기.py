#https://school.programmers.co.kr/learn/courses/30/lessons/87377

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
line = [[1, -1, 0], [2, -1, 0]]
line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]




#개인풀이 실패 
from itertools import combinations

def solution(line): 
    answer=-1
    total=[[100001,100001],[-100001,100001],[100001,100001],[-100001,-100001],[100001,-100001]]
    for l in combinations(line, 2):
        A, B, E = l[0][0],l[0][1],l[0][2]
        C, D, F = l[1][0],l[1][1],l[1][2]
        if (A*D-B*C) ==0:
            continue
        else:            
            x = (B*F-E*D)/(A*D-B*C)
            y = (E*C-A*F)/(A*D-B*C)   
        if int(x)==x and int(y)==y:
            #별 꼭지점    
            if x == 0 and total[0][1]>=y:
                total[0]=[x,y]
            #좌상단
            if x < 0 and y>0 and total[1][0] <=x and total[1][1]>=y:
                total[1]=[x,y]
            #우상단
            if x>0 and y>0 and total[2][0]>=x and total[2][1]>=y:
                total[2]=[x,y]
            #좌하단
            if x<0 and y<0 and total[3][0]<=x and total[3][1]<=y:
                total[3]=[x,y]
            #우하단
            if x>0 and y<0 and total[4][0]>=x and total[4][1]<=y:
                total[4]=[x,y]
    total= [i for i in total if abs(i[0])!=100001 and abs(i[1])!=100001]
    if len(total)==1:
        answer = ['*']
        return answer
    if len(total)==2:
        w=abs(total[0][0])+abs(total[1][0])
        answer = ['.']*int(w+1)
        answer[0]='*'
        answer[-1]='*'
        answer=[''.join(answer)]
        return answer
    else:
        #별로 표현하기
        #위 높이는 별 윗점 y값으로 정해짐
        #아래 높이는 가장 낮은 y값으로 정해짐 좌하단, 우하단 y값
        #0이 있는 줄이 있으므로 기본적으로 1씩 더해줘야함            
        h=(total[0][1]-total[1][1])+(total[1][1]-total[3][1])+1
        w=abs(min(total[1][0],total[3][0]))+abs(max(total[2][0],total[4][0]))+1
        re_total = ['.'*int(w) for hh in range(int(h)) ]
        for hh in range(int(h)):
            if hh==0:
                now = list(re_total[hh])
                now[int(w/2)] = '*'
                re_total[hh]=''.join(now)
            if hh == total[2][0]-total[1][1]:
                now = list(re_total[hh])        
                now[0]='*'
                now[-1]='*'
                re_total[hh]=''.join(now)
            if hh == h-1:
                now = list(re_total[hh])        
                now[0]='*'
                now[-1]='*'
                re_total[hh]=''.join(now)
        answer=re_total
        return answer

#풀이
#참조 https://velog.io/@edhz8888/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%ED%81%B4%EB%A6%AC-%EC%B1%8C%EB%A6%B0%EC%A7%80-10%EC%A3%BC%EC%B0%A8-%EA%B5%90%EC%A0%90%EC%97%90-%EB%B3%84-%EB%A7%8C%EB%93%A4%EA%B8%B0
def solution(line):
    INF = float('inf')
    mark,L = [],len(line)
    minx,maxx,miny,maxy=INF,-INF,INF,-INF
    for i in range(L):
        for j in range(i,L):
            if i==j : continue
            A,B,E,C,D,F = *line[i],*line[j]
            mo = A*D-B*C
            if mo==0: continue
            x,y=(B*F-E*D)/mo,(E*C-A*F)/mo
            if x-int(x) or y-int(y) : continue
            x,y=int(x),int(y)
            minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
            mark.append((x,y))
    res=[['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in mark : res[maxy-y][x-minx] = '*'
    return [''.join(s) for s in res]

INF = float('inf')
mark,L = [],len(line)
minx,maxx,miny,maxy=INF,-INF,INF,-INF
for i in range(L):
    for j in range(i,L):
        if i==j : continue
        #언패킹
        A,B,E,C,D,F = *line[i],*line[j]
        #print(*line[i],*line[j])
        mo = A*D-B*C
        if mo==0: continue
        x,y=(B*F-E*D)/mo,(E*C-A*F)/mo
        print(x,y)
        if x-int(x) or y-int(y) : continue #반드시 if문에 1이어야만 넘어가는건 아님 0만 아니면 됨 #정수가 아닌것들은 pass
        x,y=int(x),int(y)
        minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
        mark.append((x,y))
    res=[['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in mark : res[maxy-y][x-minx] = '*' #key point

print([''.join(s) for s in res])

#test
nq = [[1,2],[3,4],[5,6],[7,8]]
for i in range(len(nq)):
    for j in range(2):
        print(*nq[i],':',*nq[j])