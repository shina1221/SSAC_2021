"""
문제 : https://programmers.co.kr/learn/courses/30/lessons/17681

네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 
각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.

2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 
각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 
어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 
지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.

3. "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.

4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때
얻어지는 이진수에 해당하는 값의 배열이다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면
다음과 같이 건너야 합니다.

입출력 예제
n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
출력=["#####","# # #", "### #", "# ##", "#####"]

n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]
출력=["######", "### #", "## ##", " #### ", " #####", "### # "]

"""
def solution(n, arr1, arr2):
    #변수의 자리를 만들어주고 시작
    #왜냐하면 실제 이진수를 구하고 채우지 못한 자리가 있을 수 있기 때문
    #같은 for문 내에서 만들었다가 둘이 연동되서 에러남 반드시 따로 할 것
    total_arr1=[]
    for k in range(n):
        mini_list1=[]
        for j in range(n):
            mini_list1.append('')
        total_arr1.append(mini_list1)
    total_arr2=[]
    for kk in range(n):
        mini_list2=[]
        for jj in range(n):
            mini_list2.append('')
        total_arr2.append(mini_list2)
    for n1_num in range(len(arr1)):
        n1=arr1[n1_num]
        #세부 리스트로 들어가기 위한 숫자 
        cnt1=0
        if n1 == 0:
            #이미 만들어 뒀으므로 패스
            continue
        if n1 == 1:
            total_arr1[n1_num] = (['','','','', '#'])
            continue
        else:
            #세부리스트 맨 마지막에서 시작
            while n1 >=1: 
                #몫
                cnt1-=1
                quo1=n1//2
                #나머지
                rem1=n1%2 * '#'
                n1=quo1
                total_arr1[n1_num][cnt1]=rem1
    #print(total_arr1)
    for n2_num in range(len(arr2)):
        n2=arr2[n2_num]
        #세부 리스트로 들어가기 위한 숫자 
        cnt2=0
        if n2 == 0:
            #이미 만들어 뒀으므로 패스
            continue
        if n2 == 1:
            total_arr2[n2_num] = (['','','','', '#'])
            continue
        else:
            #세부리스트 맨 마지막에서 시작
            while n2 >=1: 
                #몫
                cnt2-=1
                quo2=n2//2
                #나머지
                rem2=n2%2 * '#'
                n2=quo2
                total_arr2[n2_num][cnt2]=rem2        
    #print(total_arr2)
    answer=[]
    for ijk in range(n):
        last_arr=[]
        for ij in range(n):
            if total_arr1[ijk][ij] =='' and total_arr2[ijk][ij]=='':
                last_arr.append(' ')
            else:
                last_arr.append('#')
        #print(last_arr)
        answer.append(''.join(last_arr))
    return answer
