def find_operation(arr):

    
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    x = sorted(arr)

    count = 0
    
    if x[0] != 0:
        for i in range(x[0]):
            x[0]-=1
            count += 1
    return count
    

n = int(input())
arr = list(map(int, input().split()))  
res = find_operation(arr)


print(res)

