"""
#문제 : https://programmers.co.kr/learn/courses/30/lessons/42577

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 
그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.

입출력 예제
phone_book	                        return
["119", "97674223", "1195524421"]	false
["123","456","789"]	                true
["12","123","1235","567","88"]	    false

입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.
"""

"""
알고리즘 스터디에서 참고로 배운 것
phone_book.sort(key = lambda x:len(x))
길이순 정렬

"""
#성공
def solution(phone_book):
    #sorting한 뒤
    phone_book.sort()
    #디폴트 값은 True로 두고 //겹치는 접미사가 없을 경우 True가 됨
    answer= True
    for i in range(len(phone_book)-1):
        #앞의숫자와 바로 뒤의 숫자의 접두사 비교 
        #string 길이를 벗어나는 위치까지 탐색을 해도 에러는 안나고 저장된 데이터만 출력됨.
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer=False
            break
    return answer    

#이하는 시행착오#####################################3

#test
phone_book = ["12","123","1235","567","88"]
def solution(phone_book):
    phone_book.sort()

    for i in phone_book
    answer=True
    return answer

testm=['132', '4567', '8654', '1325', '45678']
testm.sort()
answer=False
for i in range(len(testm)):
    ii = testm[i]
    print('first: ',ii)
    for j in range(i+1,len(testm)):
        print('?',j, testm[j])
        print(testm[j][len(ii):])
        if ii == testm[j][len(ii):]:
            answer = True
            print('second', testm[j],testm[j][len(ii):])
            break
print(answer)

#test2

testm=['132', '4567', '8654', '1325', '45678']
testm.sort()
answer=True
for i in range(len(testm)):
    ii = testm[i]
    #print('first: ',ii)
    for j in range(i+1,len(testm)):
        #print('?',j, testm[j])
        print(len(ii), ii, 'j:', testm[j])
        print('test',testm[j][:len(ii)])
        if ii == testm[j][:len(ii)]:
            answer = False
            print('second', testm[j],testm[j][len(ii):])
            break
print(answer)

#######################
#효율성 3,4에서 걸림
def solution(phone_book):
    end_point=0
    phone_book.sort()
    #전화번호 중복 접두사 유무 디폴트는 true
    answer= True
    for i in range(len(phone_book)):
        if end_point ==1:
            answer = False
            break
        ii = phone_book[i]
        for j in range(i+1,len(phone_book)):
            #비교하려는 번호의 길이만큼 다른 비교대상 번호의 접두사를 끊어서 비교
            if ii == phone_book[j][:len(ii)]:
                #만약 접두사가 동일한 것이 존재한다면 False
                end_point=1
                break
    return answer        

#####

#for문을 하나로 줄여줌
def solution(phone_book):
    end_point=0
    #sorting한 뒤
    phone_book.sort()
    answer= True
    for i in range(len(phone_book)-1):
        #앞의숫자와 바로 뒤의 숫자의 접두사 비교 
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer=False
            break
    return answer    

