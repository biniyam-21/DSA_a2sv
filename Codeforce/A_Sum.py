def summation():
    t = int(input())
    # nums = list(map(int, input().split()))

    for _ in range(t):
        nums = list(map(int, input().split()))
        mx = max(nums)
        found = False
        for i in range(len(nums)):
            if mx - nums[i] in nums:
                found = True
                break
        print("YES" if found else "NO")


summation()