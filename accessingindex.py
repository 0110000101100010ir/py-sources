#Sieve of Eratosthenes
def primes(n):
    numbers = [num for num in range(2,(n+1))]
    index = 0
    flag = True
    while flag:
        prime = numbers[index]
        #print(prime)
        flag = False
        for num in numbers:
            if num != prime and (num%prime == 0 or num == prime**2):
                numbers.remove(num)
                flag = True
                #print(numbers)
        
        index+=1
    return numbers

pnums = primes(1000)

import time

def binary_search(num,numList):
    
    min_val = 0
    max_val = len(numList)-1
    search = min_val
    
    while numList[search] != num:
        search = (max_val + min_val)//2
        if numList[search]>num:
            max_val = search - 1
        else:
            min_val = search + 1
            
    return search

tic = time.time()
print(binary_search(67,pnums)) # OUTPUT: 18
tac = time.time()
print(tac-tic) # OUTPUT: 0.00045800209045410156

tic = time.time()
print(pnums.index(67)) # OUTPUT: 18
tac = time.time()
print(tac-tic) # OUTPUT: 0.00026488304138183594
