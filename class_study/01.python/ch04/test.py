#
numbers =[273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number % 2 == 1:
        print(number, "는 홀수입니다.")
        #print('{}는 홀수입니다.'.format(number))
    else:
        print(number, "는 짝수입니다.")
        #print('{}는 짝수입니다.'.format(number))
#
for number in numbers:
    if number % in != 0:
        judge = '홀수'
    else:
        judge = '짝수'
    print('{}는 {}입니다.'.format(number, judge))
##########################################################################    
for number in numbers:
    print('{}는 {}자릿수 입니다.'.format(number, len(str(number))))
    
#4번
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
]

for list in list_of_list:
    for ele in list:
        print(ele)

# 5번#########################################################################
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[(number-1)%3].append(number)
    #output[(number-1)//3) ].append(number)

print(output)


############if
numbers=['a','b',3,'hello']
count=0
#enumerate를 쓰면 순서를 받을 수 있음

numberss=[100,2,5,11]
for i. number in enumerate(numberss):
    print(i,number)

for number in enumerate(numbers):
    output[(number-1)%3].append(number)
    output[count%3].append(number)

print(output)