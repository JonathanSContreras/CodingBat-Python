# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. If there are multiple copies of the 
# smallest value, ignore just one copy, and likewise for the largest value. 
# Use int division to produce the final average. You may assume that the array is length 3 or more.
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    nums = sorted(nums)
    nums = nums[1:-1]
    for i in range(len(nums)):
        bruh = nums[i] /2 
        if len(nums)%2==1: 
            return nums[int(len(nums) / 2) ]
        if len(nums)%2==0:
            first_middle = nums[int(len(nums) / 2) - 1] # = 3 - 1 = 2
            second_middle = nums [int(len(nums) / 2)]
            return int((first_middle + second_middle)/2)
        return int(bruh)
print(centered_average([-10, -4, -2, -4, -2, 0]))