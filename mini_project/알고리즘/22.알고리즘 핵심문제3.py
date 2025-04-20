#캠핑
#https://www.acmicpc.net/problem/4796

#풀이
import sys
input=sys.stdin.readline

tc=1
while True:
    L,P,V = map(int,input().split())
    if L == 0:
        break

    print(f'Case {tc}: {V//P *L +min(L, V%P)}')
    tc+=1

#내 풀이 실패
import sys

# L = 사용가능일 수, P = 캠핑 연속하는 일 수, V = 휴가일 수
def chk_def(L,P,V):
    global cnt
    case_answer=0
    cnt+=1
    #내 휴가로 캠핑장을 이용할 수 있을 때
    if V-(V//P)*L >0:
        #우선순위 연산자에 의해 //가 *보다 우선
        case_answer+=(V//P)*L
        case_answer+=(V-(V//P)*P)
        #우선순위 연산자에 의해 // 다음 * 다음 -
        #print('case %d' % cnt)
        # 정수	    %d 
        # 실수  	%f
        # 문자열	%s
        # 8진수	    %o
        # 16진수	%x
        # %	        %%
        
        #print('case {0}'.format(cnt))
        #print('case {0} {1}'.format(cnt, '그러하다))

        #3.6버전부터 가능        
        print(f'case {cnt}: {case_answer}')
    else:
        #elif와 else는 단독사용 불가, else는 위의 모든 조건식이 거짓일 때 
        #휴가일에 캠핑장을 사용하지 못할 경우
        #ex) 사용가능1일 캠핑장1일 휴가2일
        print(f'case {cnt}: 0')
    return   


def chk_def(L,P,V):
    global cnt
    case_answer=0
    cnt+=1
    if V-(V//P)*L >0:
        case_answer+=(V//P)*L
        case_answer+=(V-(V//P)*P)    
        return print(f'case {cnt}: {case_answer}')
    elif V-:
    else:
        return print(f'case {cnt}: 0')

check=1
cnt=0
while True:
    #map 함수는 반환으로 map 객체를 하기 때문에 자료형을 list 혹은 tuple로 변환시켜야함.
    total_list = list(map(int, sys.stdin.readline().rstrip().split()))
    L, P, V = total_list [0], total_list [1], total_list [2]  
    if L==0 and P==0 and V==0:
        break
    chk_def(L,P,V)

#다시 또 틀림
def chk_def(L,P,V):
    global cnt
    cnt+=1
    if V%P>0:
        if V//P > 0:
            if (V-(V//P)*P)<L:
                case_answer=((V//P)*L)+(V-(V//P)*P)
                print(f'case {cnt}: {case_answer}')
            else:
                case_answer=(((V//P)*L)+L)
                print(f'case {cnt}: {case_answer}')
        else:
            if V>L:
                print(f'case {cnt}: {L}')
            
            else: #L>V
                print(f'case {cnt}: {V}')
    else:
        print(f'case {cnt}: {(V//P)*L}')

#다시 또 틀림
def chk_def(L,P,V):
    global cnt
    cnt+=1
    if V%P>0:
        if V//P > 0:
            if (V-(V//P)*P)<L:
                case_answer=((V//P)*L)+(V-(V//P)*P)
                print(f'case {cnt}: {case_answer}')
            else:
                case_answer=(((V//P)*L)+L)
                print(f'case {cnt}: {case_answer}')
        else:
            if V>L:
                print(f'case {cnt}: {L}')
            
            else: #L>V
                print(f'case {cnt}: {V}')
    else:
        print(f'case {cnt}: {(V//P)*L}')



















        if V>L:
            case_answer+=(V//P)*L
            case_answer+=(V-(V//P)*P)    
            return print(f'case {cnt}: {case_answer}')
        else:
            return print(f'case {cnt}: {}')

    else:
        if L>(V-(V//P)*P):
            case_answer+=(V//P)*L
            case_answer+=V-(V//P)*P
        else:
            case_answer+=(V//P)*L+L


        return print(f'case {cnt}: {(V//P)*L}')

check=1
cnt=0
while True:
    #map 함수는 반환으로 map 객체를 하기 때문에 자료형을 list 혹은 tuple로 변환시켜야함.
    total_list = list(map(int, sys.stdin.readline().rstrip().split()))
    L, P, V = total_list [0], total_list [1], total_list [2]  
    if L==0 and P==0 and V==0:
        break
    chk_def(L,P,V)




