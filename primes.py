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

print(primes(1000))
