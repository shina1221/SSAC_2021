"""
1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
예시)
가로의 숫자를 입력하시오 : 4
세로의 숫자를 입력하시오 : 4
"""
import numpy as np
#가로
width_len=int(input('가로의 숫자를 입력하시오:')) 
#세로
length_len=int(input('세로의 숫자를 입력하시오:'))

for ll in range(length_len):
    print('*' * width_len)
   
#삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오

def triangle(width_len, length_len):
    return width_len*length_len*0.5

triangle(width_len,length_len)

"""
3. 아래와 같이 별이 찍히게 출력하시오
숫자를 입력하세요 : 
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★
"""

number=int(input('숫자를 입력하세요:'))
cnt=0


while cnt<number:
    print(('*'*(cnt+1)).center(5,' '))
    if cnt==4:
        for j in range(3,-1,-1):
            print(("*"*(j+1)).center(5," "))
    cnt+=1
    

    
