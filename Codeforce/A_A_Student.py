def solve():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        A = max(0, max(b, c) - a + 1)
        B = max(0, max(a, c) - b + 1)
        C = max(0, max(a, b) - c + 1)
        results.append(f"{A} {B} {C}")

        # results.extend(A, B, C)
    
    # print("".join(results), end=" ")
    return " \n".join(results)

m = solve()
print(m)