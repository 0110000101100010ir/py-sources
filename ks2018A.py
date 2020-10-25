def Check(N):
    digit_list = list(str(N))
    index = 0
    for digit in digit_list:
        if not int(digit)%2 == 0:
            return False, digit, index, digit_list
        index+=1
    return (True,)

def doplus(N):
    odd, index, digit_list = Check(N)[1:]
    if len(digit_list)==1 or int(digit_list[index]) > 8:
        return -1
    if not Check(N)[0]:
        
        odd = int(odd) + 1
        digit_list[index] = str(odd)
        for idx in range(index+1,len(digit_list)):
            digit_list[idx] = '0'
        Y = int("".join(digit_list))
        return Y - N

def dominus(N):
    if not Check(N)[0]:
        odd, index, digit_list = Check(N)[1:]
        odd = int(odd) - 1
        digit_list[index] = str(odd)
        for idx in range(index+1,len(digit_list)):
            digit_list[idx] = '8'
        X = int("".join(digit_list))
        return N - X

def Supervin(N):
    if Check(N)[0]:
        return 0
    else:
        if doplus(N) < 0:
            return dominus(N)
        elif dominus(N) < doplus(N):
            return dominus(N)
        elif dominus(N) > doplus(N):
            return doplus(N)
        else:
            return dominus(N)
    


T = int(input())
N_list = list()
while T>0:
    N_list.append(int(input()))
    T -= 1
case = 1
for N in N_list:
    print("Case #{}: {}".format(case,Supervin(N)))
    case += 1
