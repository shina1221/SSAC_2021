## 깊이우선탐색 & 너비우선탐색

# 깊이우선탐색(DFS)
-Depth First Search의 약자로 넓이 우선탐색 의미
하나의 경우의 수에 대해 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정

    #구조
              (1)A
       |       |       |
    (2)B      (8)C    (11)D   
    |  |       |       |   \
  (3)E (5)F   (9)G    (12)H (14)I
  |    |  |    |       |   \
(4)J (6)K (7)L (10)답 (13)N (15)O 

# 스택의 깊이우선 탐색 활용
 
                               (검사한 요소 제외)
                            (아래 남아있는 요소 추가)
              검사중인 요소의    한쪽방향에서만  
     검사중   밑에 있는 요소들  접근가능한 스택 
        A         [B,C,D]      >    [B,C,D]
       
        B         [C,D]        >    [E,F,C,D]

        E         [J]          >    [J,F,C,D]

        J         []           >    [F,C,D]

        F         [C,D]        >    [K,L,C,D]

        K         []           >    [L,C,D]

        L         []           >    [C,D]

        C         [G]          >    [G,D]

        G         [정답]       >    [D]


# 깊이우선탐색(DFS) 구현

- ex)미로찾기

    좌 0 1 2 3 4 5 
    0  0 0 0 0 0 0
    1  1 0 1 1 1 0
    2  0 0 1 0 1 0
    3  0 1 1 0 0 0
    4  0 0 1 1 1 1 
    5  1 0 0 0 0 0 >도착
    
                              
               접근가능한    
     검사중      좌표들       
      [0,0]      [[0,1]]     <접근가능 좌표의 가장 마지막을 빼옴
       
      [0,1]   [[1,1],[0,2]]      

      [0,2]   [[1,1],[0,3]]  

      [0,3]   [[1,1],[0,4]]  

      [0,4]   [[1,1],[0,5]]  

      [0,5]   [[1,1],[1,5]]  

      [1,5]   [[1,1],[2,5]]  

      [2,5]   [[1,1],[3,5]]  

      [3,5]   [[1,1],[3,4]]  

      [3,4]   [[1,1],[3,3]]  

      [3,3]   [[1,1],[2,3]]  
      
      [2,3]   [[1,1]]  

      [1,1]   [[2,1]]

      [2,1]   [[2,0]]

      [2,0]   [[3,0]]

      [3,0]   [[4,0]] 

      [4,0]   [[4,1]]           

      [4,1]   [[5,1]]           

      [5,1]   [[5,2]]                 

      [5,2]   [[5,3]]           

      [5,3]   [[5,4]] 

      [5,4]   [[5,5]]  
      
      [5,5]   []             #True 반환 뒤 종료

# 깊이우선탐색(DFS) 예시코드

while len(stack)>0:                  #스택에 데이터가 있다면                             
    if now == dest(목적지):          #정답여부 검사      #스택의 가장 마지막 데이터 추출
        return True: #도착                               #now는 현재위치 
    x=now[1]                                             #x는 오른쪽과 왼쪽방향을 나타냄
    y=now[0]                         #정답여부 검사      #y는 위 아래 방향을 나타냄
    if x -1 > -1:                    #왼쪽으로 이동할 수 있다면    # x값은 왼쪽방향으로 갈 때 인덱스를 벗어나지 않는다면
        if maps[y][x-1]==0:                                        # 갈 수 있는 길이라면
            stack.append([y,x-1])                                  # 기존값을 스택에 담고
            maps[y][x-1]=2           #왼쪽으로 이동할 수 있다면    # 방문여부 2로 표시 //이렇게 새로 갱신하지 않으면 무한루프에 빠질 수 있음
        if x + 1 < hori:             #오른쪽으로 이동할 수 있다면  # hori는 오른쪽으로 이동했을 때 벗어나는 범위 기준 
            if maps[y][x+1]==1:      
                stack.append([y,x+1])
                maps[y][x+1]=2       #오른쪽으로 이동할 수 있다면  
        if y - 1 > -1:               #위로 이동할 수 있다면
            if maps[y-1][x]==1:      
                stack.append([y-1,x])
                maps[y-1][x]=2       #위로 이동할 수 있다면
        if y + 1 < verti:            #아래로 이동할 수 있다면
            if maps[y+1][x]==1:      
                stack.append([y+1,x])
                maps[y+1][x]=2       #아래로 이동할 수 있다면 
    return False                     #스택에 데이터가 없으면 False


# 너비우선탐색(BFS)

    #구조
              (1)A
       |       |       |
    (2)B      (3)C    (4)D   
    |  |       |       |   \
  (5)E (6)F   (7)G    (8)H (9)I
  |    |  |    |       |   \
(10)J (11)K (12)L (13)답 (14)N (15)O 

# 큐의 너비우선 탐색 활용
 
              검사중인 요소의              양쪽방향에서 
     검사중   동레벨에 있는 요소들         접근가능한 큐 
        A         []               >    정답이 있다면 종료,
                                           없으면 레벨로 
        B         [C,D]            >    
       
        E         [F,G,정답,H,I]   >    정답발견, 종료
                                        

=====================================================================
                                                (선입선출) 
                검사중인 요소의             해당 위계요소가 정답이  
     검사중   동레벨에 있는 요소들       아니라면 아래 위계 요소 추가
        A             []             >            [B,C,D]
                                     
        B             [C,D]          >            [C,D,E,F]   //B 아래의 요소 추가
       
        C             [D]            >            [D,E,F,정답]               

        D             []             >            [E,F,정답,H,I] 

        E             [F,정답,H,I]   >            [E,F,정답,H,I,J] 

        F             [정답,H,I]     >            [정답,H,I,K,L] 

        정답          [H,I]            >          정답발견, 종료
                                        

# 너비우선탐색(BFS) 구현

- ex)최단경로찾기
 1 - 2 - 3 - 4 ㄱ
 | \   / | \ |  |
 5 - 6 - 7 - 8  |
 |     /   /   /  
 9 - 10  11  12 - 도착 
        /   \ 
       5     2
(두번째   (첫번째 
 줄의 5)   줄의 2)

1번 섬에서부터 12번 섬까지 가는 최단 경로는 얼마인가?

#큐에는 데이터간 섬과의 거리 요소 갯수가 들어감
#각 섬의 거리는 1
#1번 검사시 1번과의 거리는 0이므로 거리 0의 개수는 1

검사중  
큐에는 섬과의 거리를 나타내는 요소가 동일한 것들이 몇개인지 나타내는 것

        탐색 전                 탐색 후     (거리별 요소 큐에 
 거리   거리 별                 거리 별      추가하고자 하는  
       요소들 갯수  탐색 요소  요소들개수   요소가 있다면 pass)         
                                                요소 추가
                                    
   0        1           1          0             [2,5,6]             
                                                
   1        3           2          2             [5,6,3,11]

   1        4           5          3             [6,3,11,9] 

   1        4           6          3             [3,11,9,12]

   1        4           3          3             [11,9,12,7,8]                       
 
   1        5           11         4             [9,12,7,8]

   1        4           9          3             [12,7,8,10]

   1        4           12         3             정답발견, 종료 

# 너비우선탐색(BFS) 예시코드
                                                
while len(queue)>0:                              #큐에 데이터가 있다면
    #아래의 queue는 같은 거리에 있는 큐 데이터 갯수  
    count = len(queue)                           #같은 거리에 있는 큐 개수 만큼 검사 
    for time in range(count):                    
    now = queue.pop(0)                           #같은 거리에 있는 큐 개수 만큼 검사
    if now == dest(목적지):                      #정답이 존재하면 값 반환 
        return answer                            #정답이 존재하면 값 반환 #거리값 반환
    for i in data:                               #연결된 포인트 완전 탐색
        if i[0]==now and visited[i[1]-1]==False:                           #방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
        queue.append(i[1])                       
        visited[i[1]-1]=True                       
    elif i[1]==now and visited[i[0]-1]==False:   
        queue.append(i[0])                        
        visited[i[0]-1]=True                     #연결된 포인트 완전 탐색
    answer+=1                                    #거리를 1 더 벌림
return answer     
