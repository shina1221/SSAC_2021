#다리를 지나는 트럭
"""
문제 : https://programmers.co.kr/learn/courses/30/lessons/42583

트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 
다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면
다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	                []	                []       	[7,4,5,6]
1~2	                []	                [7]      	[4,5,6]
3	                [7]	                [4]      	[5,6]
4	                [7]	                [4,5]    	[6]
5               	[7,4]	            [5]     	[6]
6~7	                [7,4,5]	            [6]     	[]
8	                [7,4,5,6]	        []	        []
"""

#성공
def solution(bridge_length, weight, truck_weights):
    #빈 다리 리스트 만들기
    bridge_list=[0]*bridge_length
    #빈 주차리스트
    parked_list=[]
    #반복문을 돌기위해 리스트 길이를 늘려줌
    for i in range(len(truck_weights)+1,len(truck_weights)+bridge_length+1):
        truck_weights.append(0)
    answer=0    
    #종료조건
    #대기 트럭이 0가 될때까지 반복
    while truck_weights!=[]: 
        #기존 다리 리스트는 고정되어 있음 
        #대기 트럭을 다리에 옮기기 위해 우선 다리의 첫번째 요소를 추출 
        wait_value=bridge_list.pop(0)
        #print(bridge_list)    
        #print(wait_value)
        #다리가 감당할 수 있는 무게를 기준으로 넣을 수 있는지 없는지 구분
        if (sum(bridge_list)+truck_weights[0])<=weight:
            # 만약 기존의 다리에 새로운 트럭을 추가해서 문제가 없을 경우
            # 새로운 트럭을 추가
            truck_input=truck_weights.pop(0)
            bridge_list.append(truck_input)
            #반복의 기준은 다리에 트럭이 움직이는 횟수임
            answer+=1
            #print('parked, ', parked_list, 'bridge',bridge_list, 'truck', truck_weights)
            #다리가 감당가능한 트럭을 움직일 수 있는 만큼 움직이고 다음 반복문으로 진행
            continue
        #기존의 다리에 더이상 새로운 트럭을 넣지 못할 경우
        else:
            #기존 다리에 있는 트럭을 앞으로 한칸씩 이동
            bridge_list.append(0)
            answer+=1
            #print('parked, ', parked_list, 'bridge',bridge_list, 'truck', truck_weights)
            #더이상 움직일 수 없으므로 다음으로  continue
            continue
    return answer


#이하는 시행착오

#1차 제출 실패

def solution(bridge_length, weight, truck_weights):
    #빈 다리 리스트 생성
    bridge_list=[0]*bridge_length
    #빈 주차리스트 생성
    parked_list=[]
    #종료조건을 위한 변수 생성
    total_truck=len(truck_weights)
    #반복문을 돌리기 위해 기존의 대기트럭 리스트 뒤에 다리길이만큼 0 추가
    for i in range(len(truck_weights)+1,len(truck_weights)+bridge_length+1):
        truck_weights.append(0)
    #브릿지 갱신
    first_truck=truck_weights.pop(0)
    bridge_list.append(first_truck) 
    bridge_list.pop(0)
    answer=1    #while len(parked_list)!=total_truck:
    #=대기중인 차가 모두 주차될 때까지 반복
    #while len(parked_list)!=total_truck:
    while truck_weights != []: 
        print('bridge_list', bridge_list)
        print('truck_weights',truck_weights)
        #새로운 요소가 추가될 예정이므로 다리에서 현재의 리스트 요소를 추출
        #다리의 길이는 일정하기 때문  
        wait_value=bridge_list.pop(0)    
        #다리에 추가적으로 트럭을 넣어서 무게를 감당할 수 있다면 
        if (sum(bridge_list)+truck_weights[0])<=weight:  
            #대기트럭 하나를 움직여서 다리에 추가
            truck_input=truck_weights.pop(0)
            bridge_list.append(truck_input)
            #다리에서 뽑았던 첫번쨰 대기값을 기준으로
            #빈 대기열이면 그냥 지나치고
            if wait_value==0:
                pass
            #빈 대기열이 아니었으면 
            else:
                #트럭 주차
                parked_list.append(wait_value)
            answer+=1
        #다리에 추가적으로 트럭을 넣어서 무게를 감당할 수 없다면
        else:  #(sum(bridge_list)+truck_weights[0])>weight
            #첫번째 값이 0이 아니라면 더이상 값을 추가할 수 없으므로
            if bridge_list[0]!=0:
                bridge_list.append(0)
            #첫번째 값이 0이 라면
            else:
                #바로 대기트럭 추가
                bridge_list.append(truck_input)
            answer+=1
    return answer

#===================================
# 2차 제출시 실패
def solution(bridge_length, weight, truck_weights):
    #빈 다리 리스트 생성
    bridge_list=[0]*bridge_length
    #빈 주차리스트 생성
    parked_list=[]
    #종료조건을 위한 변수 생성
    total_truck=len(truck_weights)
    #반복문을 돌리기 위해 기존의 대기트럭 리스트 뒤에 다리길이만큼 0 추가
    for i in range(len(truck_weights)+1,len(truck_weights)+bridge_length+1):
        truck_weights.append(0)
    #브릿지 갱신
    first_truck=truck_weights.pop(0)
    bridge_list.append(first_truck) 
    bridge_list.pop(0)
    answer=1    #while len(parked_list)!=total_truck:
    #=대기중인 차가 모두 주차될 때까지 반복
    #while len(parked_list)!=total_truck:
    while truck_weights != []: 
        print('bridge_list', bridge_list)
        print('truck_weights',truck_weights)
        #새로운 요소가 추가될 예정이므로 다리에서 현재의 리스트 요소를 추출
        #다리의 길이는 일정하기 때문  
        wait_value=bridge_list.pop(0)    
        #다리에 추가적으로 트럭을 넣어서 무게를 감당할 수 있다면 
        if (sum(bridge_list)+truck_weights[0])<=weight:  
            #대기트럭 하나를 움직여서 다리에 추가
            truck_input=truck_weights.pop(0)
            bridge_list.append(truck_input)
            #다리에서 뽑았던 첫번쨰 대기값을 기준으로
            #빈 대기열이면 그냥 지나치고
            if wait_value==0:
                pass
            #빈 대기열이 아니었으면 
            else:
                #트럭 주차
                parked_list.append(wait_value)
            answer+=1
        #다리에 추가적으로 트럭을 넣어서 무게를 감당할 수 없다면
        else:  #(sum(bridge_list)+truck_weights[0])>weight
            #첫번째 값이 0이 아니라면 더이상 값을 추가할 수 없으므로
            if bridge_list[0]!=0:
                bridge_list.append(0)
            #첫번째 값이 0이 라면
            else:
                #바로 대기트럭 추가
                bridge_list.append(truck_input)
            answer+=1
    return answer

#질문참조 테스트케이스
truck_weights=[2, 2, 2, 2, 1, 1, 1, 1, 1]
bridge_length=5
weight=5
solution(bridge_length,weight,truck_weights)