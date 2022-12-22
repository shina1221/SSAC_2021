#https://school.programmers.co.kr/learn/courses/30/lessons/12899
from itertools import product
#product는 중복순열

ii=[1,2,3,4,5]
dat=product(ii,repeat=2)#repeat라고 명시해줘야함
[i for i in product(ii,repeat=2)]

#중복 가능한 n개에서 r개릁 택해 일렬로 나열하는 경우의 수는 n^r
"""

"""

cnt=0
n=50000000
#50000000기준 
nn=n
while True:
    if nn<1:
        break
    cnt+=1
    nn=nn**1/3   

past=3
before_len_list=[3]
chk_cnt=1
for cntt in range(2,cnt):
    before_len_list.append(before_len_list[chk_cnt-1]+(3**cntt))
    chk_cnt+=1
    past=3**cntt

#[3, 12, 39, 120, 363, 1092, 3279, 9840, 29523, 88572, 265719, 797160, 2391483, 7174452, 21523359, 64570080]

[cntt for cntt in before_len_list if n<=cntt][0]
ba_cnt=0
before, after= [ba_cnt if n<cntt else ba_cnt+=1 for cntt in before_len_list][0],[cntt for cntt in before_len_list if n<=cntt][0]

left_n =min(n-before_len) #앞에서 가까운지, 뒤에서 가까운지

if left_n < (3**cnt)*1/2:
    #그대로
    #[i for i in product(ii, repeat=cnt)]
    for_l = product(ii, repeat=cnt)
else:
    for_l = reversed([i for i in product(ii, repeat=cnt)])
    chk_len=3**cnt
    reversed_left_n=chk_len-n

for now,ii in enumerate(for_l):
    print(i)
