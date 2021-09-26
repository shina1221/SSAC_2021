counter =0

def fibonacci(n):
    print(('fibonacci({})를 구합니다.'.format(n)))
    global counter
    counter +=1

    if n in (1,2): #n이가 1이거나 2일때
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print('------')
print('fibonacci(10)의 호출횟수: {}'.format(counter))

########################################################
counter =0

def fibonacci(n):
    print(('fibonacci({})를 구합니다.'.format(n)))
    #global counter
    global counter 
    counter +=1

    if n in [1,2]: #n이가 1이거나 2일때
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print('------')
print('fibonacci(10)의 호출횟수: {}'.format(counter))

#######################################################

