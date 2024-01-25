# Question
# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  # Sort the array
        i, j = 0, len(nums) - 1
        operations = 0

        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                operations += 1  # Found a valid pair, increment the count
                i += 1
                j -= 1
            elif sum < k:
                i += 1  # Need a larger sum, move the left pointer to the right
            else:
                j -= 1  # Need a smaller sum, move the right pointer to the left

        return operations
