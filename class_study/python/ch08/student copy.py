class Student:
    count=0 
    students =[]
    def __init__(self, name, korean, math, english, science):
        #인스턴스 변수 초기화
        self.name = name,
        self.__korean = korean,
        self.__math = math,
        self.english = english,
        self.science = science
#게터와 세터 추가요망
        def get_



        Student.count +=1
        print('{}번째 학생이 생성됨'.format(Student.count))

    def __str__(self):
        return '학생 {}입니다'.format(self.name)
#    def show(self):
#        print(학생)
#        print('name: '.format(self.name)
    def show(self):
        print('학생')
        print('name: '.format(self.name))

hong = Student('hong', 100,100,100,100)
print(hong)
print(hong.name)

#hong.show() #error

def my_sum(x,y):
    return x+y

hong.sum - my_sum(1,2)


hong =Student('홍길동', 10, 20, 30, 40)
jang =Student('장보고', 10, 20, 30, 40)

#인스턴스 변수
hong.name
jang.name

#

class HighStudent(Student):
    def __init__(self, name, korean, math, english, science, dream):
        super().__init__(name, korean, math, english, science)
        #super 안넣어주면  self.name=name부터 일일이 다 넣어줘야 함
        self.dream = dream
    def hello(self):
        print('안녕 난 고등학생이야')
    def show(self):
        self.hello()
        print('다음에 또 만나')

hong = HighStudent('홍', 10,20,20,30,'의적')
jang = Student('장', 20,30,40,50)
print(isinstance(hong,HighStudent))
#hong은 Student의 객체이기도 함
print(isinstance(hong,Student))
#True

print(type(hong) == type(Student))

print(isinstance(hong,Student))
print(isinstance(jang,HighStudent))
#Flase #학생은 맞는데 고등학생은 아님

hong.show()
jang.show()

print(hong)
print(str(hong))
print(str(jang))

#외부에서 접근 불가
print(hong.__korean) #error
print(jang.__korean) #error

#__로 프라이빗 변수를 수정할 때 게터와 세터 사용
