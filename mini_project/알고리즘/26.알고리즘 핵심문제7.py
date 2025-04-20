#색종이 붙이기
#https://www.acmicpc.net/problem/17136

"""
탐욕법으로 가장 큰 색종이부터 붙여나가는 방법이 효과적이라고 생각하지만
8x8의 경우 5x5부터 하기보다 4x4 2장을 활용하는게 더 나음
그렇기 때문에 다 해봐야 함.

#백트래킹 활용
"""
board = [list(map(int, input().split())) for _ in range(10)]
#최대값으로 초기화 색종이는 1x1 5장 ~ 5x5 5장으로 총 25장임
ans = 25
        # 1~5까지 사용한 색종이 개수 
paper = [0]*6


def is_possible(y, x, sz):
    #내가 고른 사이즈의 색종이가 남아있는지 확인
    if paper[sz]==5:
        return False
    #유효한 범위를 덮는지 체크
    if y + sz > 10 or x + sz > 10:
        return False
    
    #색종이 덮는 점위에 0이 있는지 확인
    #색종이 덮는곳은 모두 1이어야함
    for i in range(sz):
        for j in range(sz):
            if board[y+i][x+j] == 0:
                return False
    #위의 조건을 모두 만족했을 때 True
    return True




def mark(y,x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y+1][x+j]=v

    if v:
        #색종이 뗌//원상복구
        paper[sz] -= 1
    else:
        paper[sz] += 1 



def backtracking(y, x):
    global ans
    if y == 10: #다 돌았으면
        ans = min(ans, sum(paper))
        return

    if x == 10: #가장 오른쪽에 왔을 때 다음줄로 넘어감
        backtracking(y+1, 0)
        return

    if board[y][x] == 0: #0이면
        #다음칸으로 넘어감
        backtracking(y,x+1)
        return

    #1인 경우
    for sz in range(1,6):
        #색종이 사이즈로 덮을 수 있는지 검사
        if is_possible(y,x, sz):
            #가능하면 색종이를 덮음 0으로 마크
            mark(y,x, sz, 0)
            #다음칸으로
            backtracking(y,x+1)
            mark(y,x, sz, 1) #원상복구 #1짜리 써보고 원상복구 후 2짜리 덮고 그 다음거 덮고 반복




backtracking(0,0)
print(-1 if ans == 25 else ans)
