#예외고급

"""
# Exception 클래스
  - 모든 예외 클래스의 최상위 클래스

# 예외 클래스로 여러 예외를 조건에 따라 처리할 때
  : except Exception를 제일 마지막에 (만약 사용한다면)
  - “그물이 촘촘할수록 마지막에 쳐야한다.”

"""
numbers = [1,2,3,4,5]
try:
    number = int(input('정수 입력 >'))
    #print('원의 반지름', number)
    print('{}번쨰 요소의 값 {}'.format(number, numbers[number]))
"""
except Exception as e:
    print('뭔가 잘못됨')
    print('이유',e)
"""
except ValueError as e:
    print('값이 뭔가 잘못됨')
    print('이유', e)
except IndexError as e:
    print('인덱스 문제임')
    print('이유', e)
except Exception as e: #이 구문을 맨 위로 올릴 경우 지금 에러가 먼저 떠버림
    print('모든 에러를 다 처리할 예정') 
    #exception은 모든 에러의 어머니이므로 가장 마지막에 둬야 함

print('끝')

##################
x =11
if x > 10 :
    #미구현 To Do
    raise NotImplementedError #미구현
else:
    print('값이 10보다 작음')


##git에서 markdown으로 그림이나 글 써넣을 수 있음 xx.md로 표기