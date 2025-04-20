#팰린드롬 만들기
#https://www.acmicpc.net/problem/1213

#펠린드롬은 각 문자열들이 짝수개씩 있거나 홀수개 하나 나머지 전부 짝수개씩 된 배열
#펠린드롬이 가능한지 불가능 한지를 파악하는것이 우선

#문제풀이

#각 알파벳 종류별 갯수 저장
c = dict()
s = input()

#from collections import Counter
#c= Counter(input()) #딕셔너리 요소별 갯수세서 생성해줌
for ch in s:
    if ch in c:
        c[ch] +=1
    else:
        c[ch] = 1

#홀수개인 string의 갯수 파악
#홀수개인 string이 두개 이상이라면 아임소리 함수 출력
if sum(i % 2 for i in c.values()) > 1: 
    print("I'm Sorry Hansoo")
else:
    half=''
    # 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력 
    for k, v in sorted(c.items()):
        half += k * (v//2) #문자열도 이렇게 계산해서 붙일 수 있음 궅이 join 안써도 됨
        print('half', half)
    ans = half 
    for k, v in c.items():
        #홀수라면
        if v % 2:
            ans += k
            print('ans', ans) 
            break
    ans += ''.join(reversed(half))

print(ans)
