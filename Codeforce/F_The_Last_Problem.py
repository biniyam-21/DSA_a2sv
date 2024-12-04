def max_modified_sum():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f_sum = sum(a[i] * b[i] for i in range(n))
    max_sum = f_sum

    for center in range(n):
        left, right = center, center
        current_sum = f_sum
        while left >= 0 and right < n:
            swapped_effect = (a[right] * b[left] + a[left] * b[right]) - (a[left] * b[left] + a[right] * b[right])
            current_sum += swapped_effect
            max_sum = max(max_sum, current_sum)
            left -= 1
            right += 1

        left, right = center, center + 1
        current_sum = f_sum
        while left >= 0 and right < n:
            swapped_effect = (a[right] * b[left] + a[left] * b[right]) - (a[left] * b[left] + a[right] * b[right])
            current_sum += swapped_effect
            max_sum = max(max_sum, current_sum)
            left -= 1
            right += 1

    return max_sum



print(max_modified_sum())
