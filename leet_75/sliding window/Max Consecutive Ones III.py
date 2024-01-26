# Question

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Solution

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left, right, maxOnes, zeros = 0, 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxOnes = max(maxOnes, right - left + 1)
            right += 1
        return maxOnes

