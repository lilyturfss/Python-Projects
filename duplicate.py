# find duplicate number
'''
nums = []

amount = int(input("How many numbers? "))

for i in range(amount):
    number = int(input("Enter a number: "))
    nums.append(number)

print(nums)
length = len(nums)

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        print(nums[i])

'''
nums = [1,2,3,2,4]
'''
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(f"{nums[i]} is a duplicate")
'''
nums.sort()
for i in nums:
    if i == nums[i-1]:
        print(i)

