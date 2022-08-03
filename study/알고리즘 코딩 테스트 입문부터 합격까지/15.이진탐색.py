#이진탐색
"""
탐색전에 반드시 정렬되어있어야 함
살펴보는 범위를 절반씩 줄이면서 찾음

정렬 O(NlogN) + 이진탐색 O(logN) 결과적으로 O(NlogN)
미리 정렬되어 들어오면 이진탐색만 하면 되므로 O(logN)
"""
from bisect import bisect_left, bisect_right
# [이상 미만) 반열린 구간 

#리스트에 찾고자하는 값n과 동일한 값이 존재하면 해당 값의 인덱스 값을 반환
#bisect_left : 배열에 특정수가 여러개 존재한다면 가장 좌측에 있는 값의 인덱스를 반환
#              만약 찾고자 하는 수가 없다면 찾고자 하는 값보다 작은 수 중에서 가장 큰 수의 인덱스를 찾음
#bisect_right : 배열에 특정수가 여러개 존재한다면 가장 우측에 있는 값의 인덱스를 반환
#               만약 찾고자 하는 수가 없다면 찾고자 하는 값보다 큰 수중에서 가장 작은 인덱스-1 반환 

nums = [0,1,2,3,5,5,6,7,8,9]
n = 5 #4

print(bisect_left(nums, n))
#bisect_left(iterable, value):
print(bisect_right(nums, n)) 
#bisect_right(iterable, value):

from bisect import bisect_left, bisect_right
v= (0,1,2,3,3,6,6,6,7,8,8,9)
three=bisect_right(v,3) - bisect_left(v,3)
four=bisect_right(v,4) - bisect_left(v,4)
six=bisect_right(v,6) - bisect_left(v,6)
print(three, four, six)