"""
#문제 : https://programmers.co.kr/learn/courses/30/lessons/42576

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한 사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예제
participant	                                        completion	                                 return
["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                         "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	 "vinko"
["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                 "mislav"

입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 
완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 
완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 
완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
"""
"""
participant리스트와 completion 리스트를 비교하여
participant리스트와 달리 completion 리스트에 없는 사람은 미완주자로 인식하고 return
단, 이미 한번 completion리스트에 들어간 사람이라면 이후에 나온 동명이인 또한 미완주자로 인식하고 return
미완주자는 한명이므로 participant 리스트는 반드시 completion보다 한명 더 많음
"""

#이런 경우 고려
#par = 'a','a','d','e','f'  //'a','a','d','e','f'  
#com = 'a','a','f','d'      // a','a','d','f',0
def solution(participant, completion):    
    answer=''
    #인덱스 기준 값을 비교하기 위해 sorting
    participant.sort()
    completion.sort()
    #마라톤 경기에서 미완주자는 한명 이므로 completion 리스트는 participant 리스트에 비해 한명이 부족함
    #뒤에서 for문으로 비교를 하기위해 수를 맞춰줌
    completion.append(0)
    for i in range(len(participant)):            
        #참가자가 완주자라면
        if participant[i] == completion[i]:
            #이후에 동명이인이 탐색해도 완주자에서 검색하지 못하게 완주자 값을 바꿈
            completion[i]= -1
        #만약 인덱스 기준으로 현재 참가자와 완주자가 틀리다면
        #현재 탐색하고 있는 참가자를 미완주자로 간주
        elif participant[i] != completion[i]:            
            answer=participant[i]   
            return answer

#이하는 시행착오############################################################3

def solution(participant, completion):    
    answer=''
    #체크리스트 생성
    check_list=[]
    for i in participant:
        #print(i)
        #동명이인이 있을 경우를 먼저 탐색
        #완주자이면서 이미 한번 탐색이 되었다면 미완주자로 간주
        if i in completion and i in check_list:
            answer = i 
            #print('1',answer)
            #return answer
            break
        #새롭게 탐색하는 대상이라면 완주자인지 탐색
        #완주자가 아니라면
        if i not in completion:
            answer=i
            #print('2',answer)
            break
        #동명이인 색출을 위해 탐색한 대상 리스트에 추가
        check_list.append(i)
    return answer

#ex) 2,2,3,3,3,4와 2,2,3,3,4같은 케이스 고려
#효율성 테스트 실패  
def solution(participant, completion):    
    answer=''
    for i in participant:
        #참가자가 완주자라면
        if i in completion:
            #이후에 동명이인이 탐색해도 완주자에서 검색하지 못하게 완주자 값을 바꿈
            completion[completion.index(i)]= -1
        else:
            answer=i
            return answer



