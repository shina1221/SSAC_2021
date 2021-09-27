#내 풀이
import random
#1부터 45까지의 수를 대상으로 6개를 선택
def predict_lotto(n):
    import random
    #nonetype에러떠러 지금 처럼 추가
    lotto_list=list(range(6))
    for i in range(6):
        lotto_list[i] = random.randrange(1,45)
    if len(set(lotto_list))==6:
        print('로또번호 생성')
        return lotto_list
    else:
        predict_lotto(n)

        
predict_lotto(6)

#간혹 헛도는 구간이 존재
#########################################################################
from importlib import reload    
reload(predict_lotto)
#모듈이 실패하면 고치고 다시불러오는데 reload(predict_lotto)

lotto_list=[0]
for i in range(6):
    plus_i =random.randrange(45)
    lotto_list = lotto_list.append(plus_i)

lotto_list

###강사님 #################################
#1) 제일 단순
def get_lotto_vl():
    return [1,2,3,4,5,6]

#2)반복문 
def get_lotto_v2(): #n
    from random import randint
    lotto =[]
    while len(lotto) != 6:
        l = randint(1,45)
        if l in lotto:
            continue
        lotto.append(l)
    return lotto
#from inportlib import reload    
#모듈이 실패하면 고치고 다시불러오는데 reload(lotto)

#반복문 + 집합
def get_lotto_v3():
    from random import randint
    lotto = set()
    while len(lotto) !=6:
        lotto = lotto.union({randint(1,45)})
    return list(lotto)

#4) random.sample()
#sample은 비복원 추출
def get_lotto_v4():
    from random import sample
    return sample(range(1,45+1),6)

#로또 5장 샀음
[get_lotto_v4() for _ in range(5)]


#5)numpy 패키지 사용
def get_lotto_v5():
    import numpy as np 
    return list(np.random.permutaion(range(1, (45+1)) [:6])

#6)class
class Lotto:
    def __init__(self,n):
        self.n = n
    def make_me_rich(self):
        from random import sample
        return[sample(range(1,(45+1),6) for _ in range(self.n))]

