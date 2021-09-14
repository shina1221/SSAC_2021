"""
문제 : https://www.acmicpc.net/problem/5692

문제
상근이는 보통 사람들이 사는 것과는 조금 다른 삶을 사는 사람이다. 
상근이는 이런 사람들의 시선이 부담스럽기 때문에, 자신만의 숫자를 개발하기로 했다. 
바로 그 이름은 팩토리얼 진법이다. 팩토리얼 진법은 각 자리에 올 수 있는 숫자는 
0부터 9까지로 10진법과 거의 비슷하다. 하지만, 읽는 법은 조금 다르다. 
팩토리얼 진법에서는 i번 자리의 값을 ai×i!로 계산한다. 
즉, 팩토리얼 진법에서 719는 10진법에서 53과 같다. 그 이유는 7×3! + 1×2! + 9×1! = 53이기 때문이다.

팩토리얼 진법으로 작성한 숫자가 주어졌을 때, 10진법으로 읽은 값을 구하는 프로그램을 작성하시오. 

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 
길이가 최대 5자리인 팩토리얼 진법 숫자가 주어진다. 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 팩토리얼 진법 숫자를 10진법으로 읽은 값을 출력한다.

입출력 예

 예제 입력  예제 출력
    719         53
    1           1
    15          7
    110         8
    102         8
    0

#이렇게 입력 받는것이 아님

a='719 \   
    1 \
    15 \
    110 \
    102 \
    0'

a='719\n1\n15\n110\n102\n0'
"""      

"""
알고리즘 문제를 풀 때, 파이썬의 input()은 실행시간이 느려서 자주 시간초과가 난다. 
이럴때 sys모듈의 stdin을 사용하면 더 빠르게 input이 가능하다

input -> 개행문자를 벗겨 내어 -> 문자열로 변환 -> return
내장함수인 input()과 달리 sys.stdin은 file object이다.
사용자의 입력을 받는 buffer를 만들어 그 buffer에서 읽어들이는 것이다.

출처: https://developeryuseon.tistory.com/90 [도각도각 Dev Day]


한줄씩 읽어들이기

문제에 각 테스트 케이스는 한 줄로 이루어져 있고, 라고 되어있음

from sys import stdin
#strip으로 공백을 제거하면 readline으로 한줄씩 읽음
number = stdin.readline().strip()

문제에 입력의 마지막 줄에는 0이 하나 주어진다고 되어있음
따라서 0이 나오면 그만 계산하게 함
"""
import math
from sys import stdin
# 여러번 돌리는데 초기화 하기위해 1 지정
i=1
while i != 0:
    #string으로 입력받음
    i = sys.stdin.readline().rstrip()    
    if i == '0':
        break
    else:
        #각 string의 글자를 인자로 받아옴
        len_str_i=len(i)
        mul_i=0
        for ii in i:
            #각 string의 값과 string 갯수를 통한 팩토리얼 
            mul_i += int(ii)*math.factorial(len_str_i)
            #팩토리얼 하는데 수가 줄어들어야 하므로
            len_str_i=len_str_i-1
        mul_i

a.split(' ')
#['719', '', '', '', '', '1', '', '', '', '', '15', '', '', '', '', '110', '', '', '', '', '102', '', '', '', '', '0']




#공백제거
str_list=[i for i in a.split(' ') if i !='']

#합치기
test_a =['719', '', '', '', '', '1', '', '', '', '', '15', '', '', '', '', '110', '', '', '', '', '102', '', '', '', '', '0']
' '.join(test_a)


#팩토리얼을 구하는 방법
import math
#math.factorial(n)


result_list=[i for i in a.split(' ') if i !='']

for str_i in result_list:
    if str_i == '':
        pass
    else:
        #각 string의 글자를 인자로 받아옴
        len_str_i=len(str_i)
        mul_i=0
        for i in str_i:
            #각 string의 값과 string 갯수를 통한 팩토리얼 
            mul_i += int(i)*math.factorial(len_str_i)
            #팩토리얼 하는데 수가 줄어들어야 하므로
            len_str_i=len_str_i-1
        result_list[result_list.index(str_i)]=mul_i

' '.join(result_list)  

from sys import stdin
number = stdin.readline().strip()

import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]