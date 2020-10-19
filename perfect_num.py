# generate factors
def factors(p):
    for num in range(1,p):
        if p%num==0:
            yield num
            

# generate perfect number within a range    
def gen_perfect(low,high):
    sum_=0
    for numb in range(low,(high+1)):
        #print(numb)
        for fac in factors(numb):
            sum_+=fac
        if sum_== numb:
            yield numb
        
        sum_ = 0
        
# check whether perfect or not
def check_perfect(n):
    sum_ = 0
    for fac in factors(n):
        sum_+=fac
    if sum_==n:
        return "perfect"
    else:
        return "not perfect"
            
