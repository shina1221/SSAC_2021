#https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3
#완료

include = ["aya", "ye", "woo", "ma"] 

babbling= ["aya", "yee", "u", "maa", "wyeoo"]
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

chk=[0]*len(babbling)

for ba in range(len(babbling)):
    while len(babbling[ba])!=0:
        if  babbling[ba][:2] in include or babbling[ba][:3] in include:                
            if babbling[ba][:2] in include:
                babbling[ba]= babbling[ba][2:]
            if babbling[ba][:3] in include:
                babbling[ba]= babbling[ba][3:]
            print(ba, babbling)
            if len(babbling[ba]) == 0:
                chk[ba] = 1 
                break           
        else:    
            break


print(sum(chk))


