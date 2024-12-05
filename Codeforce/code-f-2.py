nums = [1,2,3,4]

queries = [[1,0],[-3,1],[-4,0],[2,3]]


for i in range(len(nums)):
    nums[i] = nums[i] + queries[i][0]


print(nums)
