#백준 1018. 체스판 다시 칠하기
"""
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""
import sys

#풀이
M,N=map(int,sys.stdin.readline().split())
board = [input() for _ in range(N)]
ans = 64 #초기값 넣어주기 답은 64보다 작을 수밖에 없음 가장 많이 바꿔봐야 32

def fill(y,x, bw):
    global ans 
    cnt=0
    for i in range(8):
        for j in range(8):
            if (i+j) %2: #0
                if board[y+i][x+j]==bw:
                    cnt+=1
            else: #1
                if board[y+i][x+j] !=bw:
                    cnt+=1

    ans = min(ans, cnt)

for i in range(N-7):
    for j in range(M-7):
        fill(i, j, 'B')
        fill(i, j, 'W')
print(ans)

#백준 2841 외계인의 기타 연주
#개인 실패
N, P= map(int, sys.stdin.readline().split())
ing_d=dict()
cnt=0
for _ in range(N):
    now_n, now_p = map(int, sys.stdin.readline().split())
    if now_n not in ing_d:
        ing_d[now_n]=[]
        ing_d[now_n].append(now_p)
        cnt+=1
    else:
        if ing_d[now_n].pop(0)<= now_p:
            ing_d[now_n].append(now_p)
            cnt+=1
        else:
            ing_d[now_n].append(now_p)            
            cnt+=2
    print(cnt)
print(cnt)

#풀이
import sys

input=sys.stdin.readline
N, P= map(int, input().split())
stk = [[] for _ in range(7)]
ans = 0
for _ in range(N):
    line, p = map(int, input().split())
    while stk[line] and stk[line][-1] >p:
        stk[line].pop()
        ans +=1

    if stk[line] and stk[line][-1] == p:
        continue
    stk[line].appen(p)
    ans+=1

print(ans)

m   