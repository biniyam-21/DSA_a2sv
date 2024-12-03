def min_subseqeunce():
    t = int(input())

    for _ in range(t-1):
        n = int(input())
        bits = list(map(str, input().split()))
        print(n,bits)

        for i in range(n-1):
            if bits[i] == "1":
                stack.append("1")
            elif bits[i+1] == '1':
                return False
    

            stack = []
    return stack
    
min_subseqeunce()




































# def minimum_subsequence():
#     t = int(input())  # Read number of test cases
    
#     for _ in range(t):
#         n = int(input())  # Length of the binary string
#         s = input().strip()  # The binary string
        
#         subsequences = []  # List to store subsequences
#         result = [0] * n  # Array to store subsequence numbers for each character
        
#         # The index of the subsequence to which each character will be assigned
#         for i in range(n):
#             assigned = False
#             # Try to fit the current character into existing subsequences
#             for j in range(len(subsequences)):
#                 if subsequences[j][-1] != s[i]:  # Ensure alternating
#                     subsequences[j].append(s[i])
#                     result[i] = j + 1  # Store the subsequence index
#                     assigned = True
#                     break
#             # If no subsequence could be found, start a new subsequence
#             if not assigned:
#                 subsequences.append([s[i]])
#                 result[i] = len(subsequences)  # Assign a new subsequence number
        
#         # Output the result for this test case
#         print(len(subsequences))  # Number of subsequences
#         print(" ".join(map(str, result)))  # Subsequence assignments for each character

# # Call the function to execute the solution
# minimum_subsequence()
