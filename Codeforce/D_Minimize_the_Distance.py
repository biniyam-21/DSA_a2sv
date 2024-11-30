def minimize():
    n = int(input().strip())
    coordinate = list(map(int, input().split()))
    coordinate.sort()
    minimum = coordinate[(n - 1) // 2]
    return minimum
 
print(minimize())