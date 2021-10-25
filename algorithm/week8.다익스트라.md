# 최단경로

# 최단경로
#플로이드 와샬 알고리즘
-모든 노드를 최단거리(최소비용)로 방문하는 알고리즘

# 다익스트라 알고리즘
- 특정 노드에서 다른 노드까지의 최단 경로 알고리즘

# 플로이드 와샬 알고리즘

비용배열과 방문배열을 만들어둠
모든노드를 연결하는 것이 목적이므로 시작점은 어느것이든 상관없음
               0   ,   1   ,   2   ,   3   ,   4   ,   5
비용배열 = [maxsize,maxsize,maxsize,maxsize,maxsize,maxsize]

              0  ,  1  ,  2  ,  3  ,  4  ,  5
방문배열 = [False,False,False,False,False,False]

위의 값으로 시작
(괄호는 비용)

            0
          / | \
     (3)/   |   \(10)
      /     |     \ 
  -- 4      |      5 --
  |   \     |(7)  /    |
  | (2) \   |    / (6) | 
  |      \  |   /      |
  |          1         |(9)
   \        |   \ (4)  | 
     \  (10)|    |     |
 (11)  \    |    2     |
         \  |  /(2)    |  
             3  --------

# 시작점이 0이라고 할 경우

0기준   1회  0,          1,       2,       3,       4,       5 
            [0,    maxsize, maxsize, maxsize, maxsize, maxsize]
            [True,   False,   False,   False,   False,   False] #방문하지 않은 노드중 최소 연결비용을 가지는 노드를 True로 변경

4기준   2회  0,        1,       2,       3,    4,     5                                       
            [0,        7, maxsize, maxsize,    3,    10]
            [True, False,   False,   False, True, False]

4기준   3회  0,        1,       2,       3,    4,     5                                     
            [0,    [7,2], maxsize,      11,    3,    10]  >>  [0,     [2], maxsize,      11,    3,    10]
                                                              [True, True,   False,   False, True, False]       

1기준   3회  0,      1,       2,          3,    4,      5                                     
            [0,    [2],       4,   [10, 11],    3,  [6,10]]  >>  [0,       2,    4,    10,    3,     6]
                                                                 [True, True, True, False, True, False]      
                                                                  
2기준   4회  0,   1,   2,    3,   4,   5                                     
            [0,   2,   4,  [10,2],  3,   6]  >>  [   0,   2,    4,    2,     3,     6]
                                                 [True, True, True, True, True, False]      

3기준   5회  0,   1,   2,   3,   4,     5                                     
            [0,   2,   4,   2,   3,  [6,9]]  >>  [   0,   2,    4,    2,     3,    6]
                                                 [True, True, True, True, True, True]       #더이상 방문할 노드가 없으므로 종료

총 비용= 0+2+4+2+3+6 =17

# 플로이드 와샬 예시코드
values = [2**31-1 for i in range(n)]                #비용배열, 거리배열 선언
visited = [False for i in range(n)]
start = 0                                           #0번 노드를 시작점으로 설정
visited[start]=True
values[start]=0
while False in visited:                             #방문하지 않은 노드가 있다면
    for i in costs:                                 #노드 완전탐색으로 비용배열의 거리 값 최소화
        if(visited[i[1]]==False and i[0]==start):
            values[i[1]]=min(values[i[1], i[2]])
        if visited[i[0]]==False and i[1]**start
            values[i[0]]==min(values[i[0]], i[2])

    refer = 2**31-1
    for i in range(n):                               #방문하지 않은 노드 중 최소비용 노드 위치 탐색 
        if(visited[i]==False and values[i]!=0):      
            refer = min(refer, values[i])            
    answer = answer + refer                          #방문하지 않은 노드 중 최소비용 노드 위치 탐색
    for i in range(n):                               #해당 노드 방문 여부 체크
        if(visited[i]==False and values[i]==refer):  
            visited[i]=True                          
            start=1                                  #해당 노드 방문 여부 체크 
            break


# 다익스트라 알고리즘

            0
          / | \
     (3)/   |   \(10)
      /     |     \ 
  -- 4      |      5 --
  |   \     |(7)  /    |
  | (2) \   |    / (6) | 
  |      \  |   /      |
  |          1         |(9)
   \        |   \ (4)  | 
     \  (10)|    |     |
 (11)  \    |    2     |
         \  |  /(2)    |  
             3  --------



# 시작점이 0이라고 할 경우

0기준   1회  0,          1,       2,       3,       4,       5 
            [0,    maxsize, maxsize, maxsize, maxsize, maxsize]
            [True,   False,   False,   False,   False,   False] #방문하지 않은 노드중 최소 연결비용을 가지는 노드를 True로 변경

#0번노드에서 연결 가능한 노드들을 봄
0기준   1회  0,          1,       2,       3,      4,       5 
            [0,        [7], maxsize, maxsize,    [3],    [10]]
            [True,   False,   False,   False,   True,   False] 

4기준   2회  0,          1,       2,       3,      4,       5 
            #현재 노드에 비용값을 더해줘야 함
            [0,    [7,3+2], maxsize,    3+11,    [3],    [10]]   >>  [   0,     5, maxsize,    14,    3,    10]
            [True,   False,   False,   False,   True,   False]       [True, False,   False, False, True, False] 

1기준   3회  0,          1,       2,       3,      4,       5 
            #현재 노드에 비용값을 더해줘야 함
            [0,       5,  [5+4],  [14,5+10],     3,   [10,5+6]]   >>  [   0,    5,     9,    14,    3,    10]
            [True, True,  False,      False,  True,      False]       [True, True, False, False, True, False]            

2기준   4회     0,     1,     2,           3,    4,     5 
            #현재 노드에 비용값을 더해줘야 함
             [   0,    5,     9,    [14,9+2],    3,    10]   >>  [   0,    5,     9,    11,    3,    10]
            #2번을 탐색해서 변경  
             [True, True,  True,       False, True, False]       [True, True, True, False, True, False]            

5기준   5회  0,          1,       2,       3,      4,       5 
            #현재 노드에 비용값을 더해줘야 함
             [   0,    5,     9,   [11,10+9],    3,    10]   >>  [   0,    5,     9,    11,    3,    10]
            #5번을 탐색해서 변경  
             [True, True,  True,       False, True,  True]       [True, True, True, False, True, False]                       
3기준   6회  0,          1,       2,       3,      4,       5 
            #현재 노드에 비용값을 더해줘야 함
             [   0,    5,     9,   11,    3,    10]   >>  [   0,    5,     9,    11,    3,    10]
            #3번을 탐색해서 변경  
             [True, True,  True,  True, True,  True]   #더이상 탐색할 노드가 없으므로 종료 

0번 노드까지의 최단경로 0
1번 노드까지의 최단경로 5
2번 노드까지의 최단경로 9
3번 노드까지의 최단경로 11
4번 노드까지의 최단경로 3
5번 노드까지의 최단경로 10


# 다익스트라 예시코드
visited = [False for _ in range(n)]                    #비용 배열, 거리 배열 선언
cost = [sys.maxsize for _ in range(n)]
visited[0] = True
cost[0] = 0                                            #0번 노드를 시작점으로 설정
length = len(visited)
while False in visited:                                #방문하지 않은 노드가 있다면
    checkLoc = -1
    checkvalue = sys.maxsize                           #방문하지 않은 지역 중 최솟값 찾기
    for i in range(length):
        if visited[i]==False and cost[i] < checkvalue:
            checkLoc = i
            checkvalue = cost[i]                       #방문하지 않은 지역 중 최솟값 찾기
    if checkLoc == -1:                                 #검사할 후보가 없다면 탈출         
        break
    visited[checkLoc] = True                           #검사할 후보가 없다면 탈출
    if v1== checkLoc and visited[v2]:                  #경로 완전탐색으로 비용배열 수정  
        cost[v2] = min(cost[v2], cost[v1]+c)
    if v2 = checkLoc and visited[v1]== False
        cost[v1] = min(cost[v1], cost[v2]+c)           #경로 완전탐색으로 비용배열 수정

