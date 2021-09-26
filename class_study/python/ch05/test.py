free = 10

print('전역 변수 : {}'.format(free))

def test():
    #free = 20  이렇게 넣는 순간 지역변수가 됨
    print('전역이면서 자유 변수: {}'.format(free))

test()


#
free = 10 
def test():
    free = free+ 20  #unbound local error   여기나온 모든 free는 맨 위의 전역변수라고 보기에 오류가 남
    print('전역이면서 자유 변수: {}'.format(free))

test()
#파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조할 수 없음

##################33
free = 10 

def test():
    global free #전역변수에 접근하기 위해 사용
    free = free+ 10
    print('전역 변수 free: {}'.format(free))

test()

print('test()실행 후 free = {}'.format(free))


#nonlocal########################
def test():
    nlocal=200

    def test_in_test():
        x=10
        nonlocal nlocal
        print('전역변수 free: {}'.format())
#쓰다말음

#############################3
free =10
print('전역 변수 free: {}'.format(free))

def test():
    #global free #전역변수
    free =200 #local

test()
print('test() 실행 후 free = {}'.format(free))
