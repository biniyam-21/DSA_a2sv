def binary_reduction():
    n = int(input())
    b = list(input().strip())
    
    stack = []
    
    for char in b:
        if stack and ((stack[-1] == '0' and char == '1') or (stack[-1] == '1' and char == '0')):
            stack.pop()
        else:
            stack.append(char)
    
    print(len(stack))

binary_reduction()































# def min_remaining_length(n, s):
#     # Convert the string to a list for easier manipulation
#     s = list(s)
    
#     # Keep reducing the string until no more pairs can be removed
#     while True:
#         found_pair = False
#         # Iterate through the string and look for adjacent "01" or "10" pairs
#         for i in range(len(s) - 1):
#             if (s[i] == '0' and s[i + 1] == '1') or (s[i] == '1' and s[i + 1] == '0'):
#                 # Remove the pair by deleting the two adjacent elements
#                 s.pop(i)
#                 s.pop(i)  # Remove the next element, which will now be at index i
#                 found_pair = True
#                 break  # Restart the process from the beginning
#         # If no pair is found, the process is complete
#         if not found_pair:
#             break
    
#     # The length of the remaining string is the answer
#     print(len(s))

# # Reading input
# n = int(input())
# s = input().strip()
# min_remaining_length(n, s)
