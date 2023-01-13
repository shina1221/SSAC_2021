#https://school.programmers.co.kr/learn/courses/30/lessons/12973

#1차 실패
def solution(s):
    if len(s)==1:
        return 0
    else:
        for _ in s:
            s=list(s)
            for ss in range(1,len(s)):
                if s[ss]==s[ss-1]:
                    if ss==1:
                        s = s[ss+1:]
                    else:
                        s = s[:ss-1]+s[ss+1:]
                    break
            chk= set(['1' if s[ss-1]==s[ss] else '0' for ss in range(len(s))])
            if len(chk) ==1:
                return int(chk.pop())

s='cdcd'
s='baaabaa'	
#참조
#https://eda-ai-lab.tistory.com/492
#stack
def solution(s): 
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)
        elif stack[-1] == i: 
            stack.pop()
        else: 
            stack.append(i)
    if len(stack) == 0: 
        return 1
    else: 
        return 0 



