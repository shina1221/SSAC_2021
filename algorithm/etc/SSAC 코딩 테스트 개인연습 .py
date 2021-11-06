#람다 함수
def plus_ten(x):
    return x+10

plus_ten(1)

plus_ten0=lambda x: x+10
plus_ten0(2)

#클래스
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

###
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

####calculator
class Calculator:
    def __init__(self):
        self.result=0
    def add(self, num):
        self.result +=num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#객체에 숫자 지정

class FourCal :
    def setdata(self, first, second):
        self.first= first
        self.second = second

a=FourCal()
a.setdata(4,2)

a.first
a.second

#값을 바로 받아서 계산하기
class FourCal:
    def setdata(self, first, second):
        self.first= first
        self.second=second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)

a.add()

#곱하기, 빼기, 나누기 
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first - self.second
    def div(self):
        result = self.first / self.second
        return result

a=FourCal()
a.setdata(5, 2)
a.add()
a.mul()
a.sub()
a.div()

#생성자

"""
 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 
 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 
 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 
단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는
 시점에 자동으로 호출되는 차이가 있다.

따라서 이 상태로 a=FourCal()을 수행하면 오류뜸
a.setdata()호출 불가
그러므로 a = FourCal(4,2)처럼 값을 지정해 주고 시작해야 함.
"""
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first - self.second
    def div(self):
        result = self.first / self.second
        return result

a=FourCal(4,2)

a.first
a.second
a.add()
a.mul()
a.sub()
a.div()

#클래스 상속
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(3,3)
a.add()

#메서드 오버라이딩
"""
부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 
메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 
이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
"""
a= FourCal(4,0)
a.div() #오류남 정상

class safeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a = safeFourCal(4,0)
a.div()

#클래스 변수
class Family:
    lastname='kim'

Family.lastname

"""
클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다는 것을
확인할 수 있다. 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
"""
Family.lastname = '박'
Family.lastname

#거품정렬
test =[5,4,3,2,1]
print(test)
for i in range(len(test)):
    for j in range(len(test)-i-1):
        if test[j]> test[j+1]:
            test[j],test[j+1]=test[j+1],test[j]
        else:
            pass
        print(test)
