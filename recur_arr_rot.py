def rotate2(arr,d):
    if d>=len(arr):
        print("condition: d < len(arr)")
        d = int(input("Enter d: "))
        return rotate2(arr,d)
    if d<=0:
        return arr
    arr.append(arr.pop(0))
    return rotate2(arr,d-1)
    
arr2 = [1,2,3,4,5,6,7,8]
rotate2(arr2,2)
