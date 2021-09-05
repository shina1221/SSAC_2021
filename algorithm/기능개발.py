"""
#문제 : https://programmers.co.kr/learn/courses/30/lessons/42586

프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 
먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 
몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

pro=[93, 30, 55]
speed=[1, 30, 5]
return=[2,1]

pro=[95, 90, 99, 99, 80, 99]
speed=[1,1,1,1,1,1]
return=[1,3,2]
"""
#성공
def solution(progresses, speeds): 
    import math   
    answer=[]
    #리스트 요소를 줄이면서 새로운 리스트를 만드는 함수
    def mid_sol(progresses, speeds):
        #ex)100-95만큼 speed를 각 리스트 요소에 곱할 것이므로
        k=100-progresses[0]
        #단 speed가 1이므로 5번 횟수를 움직여야 함
        #여기서 나눗셈의 몫이 소숫점이 나올 수 있으므로 올림을 해줌
        multip=math.ceil(k/speeds[0])
        print('k:',k)    
        #100이상이 아닌 작업리스트요소와 합할 speed 리스트 구하기
        list_k =[speeds[i]*multip for i in range(len(speeds))]        
        print('list_k:', list_k)
        #남은리스트들에 스피드를 n번 합함
        progresses_0=list(map(sum, zip(progresses, list_k)))
        print('progresses_0:',progresses_0)
        for pro_i_num in range(len(progresses_0)):
            if progresses_0[pro_i_num] >=100:
                #제외하기 위해 특정수로 변경
                progresses_0[pro_i_num]=-1
            else:
                #그 다음 수가 100미만이라면 멈춤
                break
        #모든 for문이 돌고 난 후
        #제외해야 할 100이상의 수에 대한 갯수 (=answer에 append 해야할 갯수) 
        minus_num=progresses_0.count(-1)
        #100이상인 수를 없앤 리스트 생성
        #progresses_0=[i for i in progresses_0 if i !=-1]와 동일
        progresses_0=progresses_0[minus_num:]                               #먼저 들어온 수들 중에서 100이상인 것들만 제외 
        #print('progresses_0:',progresses_0)
        #progresses의 요소갯수에 맞춰서 리스트 재 생성
        speeds=speeds[minus_num:]
        #print('speed:',speeds)      
        return progresses_0, speeds, minus_num
    #리스트들의 값이 존재할 동안 반복         
    try:    
        while True:
            #speed를 반영한 리스트 산출 및       
            print(mid_sol(progresses, speeds))     
            progresses, speeds, minus_num = mid_sol(progresses, speeds)  #
            print('after_speed:',progresses)
            print('after_pro:', progresses)
            answer.append(minus_num)
            print('answer:',answer)
            print('======================')
    except:
        print('final')
        return answer

##이하는 시행착오

def solution(progresses, speeds):    
    answer=[]
    #리스트 요소를 줄이면서 새로운 리스트를 만드는 함수
    def mid_sol(progresses, speeds):
        #ex)100-95만큼 speed를 각 리스트 요소에 곱할 것이므로
        k=100-progresses[0]
        print('k:',k)    
        #100이상이 아닌 작업리스트요소와 합할 speed 리스트 구하기
        list_k =[speeds[i]*k for i in range(len(speeds))]        
        print('list_k:', list_k)
        #남은리스트들에 스피드를 n번 합함
        progresses_0=list(map(sum, zip(progresses, list_k)))
        print('progresses_0:',progresses_0)
        for pro_i_num in range(len(progresses_0)):
            if progresses_0[pro_i_num] >=100:
                #제외하기 위해 특정수로 변경
                progresses_0[pro_i_num]=-1
            else:
                #그 다음 수가 100미만이라면 멈춤
                break
        #모든 for문이 돌고 난 후
        #제외해야 할 100이상의 수에 대한 갯수 (=answer에 append 해야할 갯수) 
        minus_num=progresses_0.count(-1)
        #100이상인 수를 없앤 리스트 생성
        #progresses_0=[i for i in progresses_0 if i !=-1]와 동일
        progresses_0=progresses_0[minus_num:]
        #print('progresses_0:',progresses_0)
        #progresses의 요소갯수에 맞춰서 리스트 재 생성
        speeds=speeds[minus_num:]
        #print('speed:',speeds)      
        return progresses_0, speeds, minus_num
    #리스트들의 값이 존재할 동안 반복         
    try:    
        while True:
            #speed를 반영한 리스트 산출 및       
            print(mid_sol(progresses, speeds))     
            progresses, speeds, minus_num = mid_sol(progresses, speeds)  #
            print('after_speed:',progresses)
            print('after_pro:', progresses)
            answer.append(minus_num)
            print('answer:',answer)
            print('======================')
    except:
        print('final')
        return answer

progresses=[95, 95, 90, 90, 99, 99, 80, 99]
speeds=[1,1,1,1,1,1,1,1]

#모든 요소들을 다 돌고나면  
"""
ex)for_test=[1,2,3,4,5]
   for_test[5:] 
   >>> []
   이와같이 빈 리스트를 반환하므로 
   빈리스트가 나오는 순간 첫번째 요소가 없으므로
   k=100-progresses[0]에서
   list index out of range 에러를 일으킴 
   따라서 try except문으로 예외처리

#질문참조 테스트케이스
progresses=[20,99,93,30,55,10]
speeds=[5,10,1,1,30,5]
solution(progresses, speeds)
"""
    