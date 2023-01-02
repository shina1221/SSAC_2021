#https://school.programmers.co.kr/learn/courses/30/lessons/68936

#쿼드트리 참조
#http://pigbrain.github.io/datastructure/2016/01/01/QuadTree_on_DataStructure
"""
-쿼드 트리는 4개의 자식 노드를 가지는 트리 구조의 자료구조다
-쿼드 트리는 2차원의 공간을 4개의 구역(4개의 자식노드)로 재귀적으로 분할한다
-쿼드 트리는 거대한 2차원 공간을 빠르게 검색 가능하다
"""

#https://school.programmers.co.kr/learn/courses/30/lessons/68936

#풀이
#https://alreadyusedadress.tistory.com/296
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def quard(x, y, n):
        first = arr[x][y]
        
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != first:
                    print(i,j,n)
                    n //= 2
                    quard(x, y, n)
                    quard(x, y + n, n)
                    quard(x + n, y, n)
                    quard(x + n, y + n, n)
                    return
        
        answer[first] += 1
    
    quard(0, 0, n)
        
    return (answer)


#개인실패

arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

import numpy as np

tot_d = {'0':0, '1':1}


tot_d = {'0':0, '1':1}
def solution(arr):
    std_n = len(arr)/2
    chk = [[] for i in range(len(arr)//2)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < std_n and j < std_n:
                chk[0].append(arr[i][j])
            if i >= std_n and j < std_n:
                chk[1].append(arr[i][j])
            if i < std_n and j >= std_n:
                chk[2].append(arr[i][j])
            if i >= std_n and j >= std_n:
                chk[3].append(arr[i][j])
    print('middle chk', chk)
    nxt_chk=[]
    for k in range(len(chk)):
        print('k',k)
        print(k, chk[k])
        if len(chk[k])==4:
            chk['1']+=len([i for i in chk[k] if i == 1])
            chk['0']+=len([i for i in chk[k] if i == 0])
            return print([tot_d['0'], tot_d['1']])
        if len(set(chk[k]))==1:
            tot_d[str(chk[k][0])]+=1
        else:
            nxt_chk.append(chk[k])
    print('nxt_chk', nxt_chk)
    solution(nxt_chk)
        