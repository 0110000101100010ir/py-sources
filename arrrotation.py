# using python list
def rotate(arr, d):
    if d>=len(arr):
        return "stop"
    time.sleep(1) # :P
    temp = list()
    counter = 0
    while counter<d:
        temp.append(arr.pop(0))
        #print(temp)
        counter += 1
        
    for item in temp:
        arr.append(item)
    return arr    

import time
arr = [1,2,3,4,5,6,7,8,9] #sample list, items are of same type
counter = 0
var = arr[:]
while True:
    tar = rotate(arr,2)
    
    if (tar==var) or (tar=="stop"):
        break
    else:
        print(tar)
    counter += 1
    
print(counter) #always counter = len(arr) - 1 irrespective of the value of d
