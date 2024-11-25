def rearrange_list(num_cases, test_cases):
    results = []  # List to store the final answers
    
    for case in test_cases:
        n, k, list_a, list_b = case  # Unpack values for this test case
        
        list_b.sort()  # Sort list_b in increasing order
        
        # Create a list of tuples (original_index, value) from list_a
        index_value_pairs = list(enumerate(list_a))
        
        # Sort index_value_pairs based on the values in list_a
        index_value_pairs.sort(key=lambda x: x[1])
        
        # Create an empty list to store the final result
        final_list = [0] * n 
        
        # Assign sorted values of list_b to correct positions in final_list
        for i in range(n):
            original_index = index_value_pairs[i][0]  # Get original position from list_a
            final_list[original_index] = list_b[i]  # Assign sorted value from list_b
        
        # Convert final_list to space-separated string and add to results
        results.append(" ".join(map(str, final_list)))
    
    # Print all results for each test case
    print("\n".join(results))


# Read number of test cases
num_cases = int(input())

# Read input for all test cases
test_cases = []
for _ in range(num_cases):
    n, k = map(int, input().split())  # Read n and k
    list_a = list(map(int, input().split()))  # Read list_a
    list_b = list(map(int, input().split()))  # Read list_b
    test_cases.append((n, k, list_a, list_b))  # Store the test case

# Call function to process test cases
rearrange_list(num_cases, test_cases)
