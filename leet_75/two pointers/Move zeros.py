# Question
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#

# Note that you must do this in-place without making a copy of the array.

# Solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insertPos = 0
        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1
        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos += 1