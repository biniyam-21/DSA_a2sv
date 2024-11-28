def binary_flip():
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[_])
        index += 1
        a = data[_]
        index += 1
        b = data[_]
        index += 1
        
        balance = [0] * n  # Track balance of 1s - 0s
        count_1, count_0 = 0, 0
        
        # Compute balance array
        for i in range(n):
            if a[i] == '1':
                count_1 += 1
            else:
                count_0 += 1
            balance[i] = count_1 - count_0  # 1s - 0s balance
        
        flip = False  # Track if we are in a flipped state
        possible = True  # Assume transformation is possible

        # Traverse from last to first
        for i in range(n - 1, -1, -1):
            expected_bit = a[i] if not flip else ('0' if a[i] == '1' else '1')
            
            if expected_bit != b[i]:  # If bits mismatch
                if balance[i] == 0:  # We can only flip if balance is 0
                    flip = not flip  # Toggle flip state
                else:
                    possible = False
                    break
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results) + "\n")

binary_flip()