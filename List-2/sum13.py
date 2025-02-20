
# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6
def sum13(nums):
    bool = True
    if len(nums) == 0:
        return 0
    while bool:
        if 13 in nums:
            nums.remove(13)
            for i in range(len(nums)):
                if nums[i] == 13:
                    nums.remove(nums[i+1])
                nums = nums
        else:
            bool = False
    return sum(nums)
print(sum13([1,2,2,1,13,2]))